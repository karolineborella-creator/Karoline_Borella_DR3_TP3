import streamlit as st

from src.agent import criar_agente, executar_agente
from src.memory import criar_sessao

st.set_page_config(
    page_title="StockMed AI",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 StockMed AI")
st.subheader("Agente Inteligente de Gestão de Estoque Hospitalar")

st.caption(
    "Inteligência Artificial aplicada à gestão "
    "de medicamentos e materiais hospitalares."
)

with st.sidebar:
    st.header("Sobre o projeto")

    st.info(
        "Agente desenvolvido com Python, LangChain, "
        "LangGraph, OpenAI e Streamlit."
    )

    st.markdown("### Funcionalidades")
    st.markdown("""
- Consulta de estoque
- Identificação de estoque crítico
- Cálculo de cobertura
- Controle de validade
- Estimativa de reposição
- Memória conversacional
    """)

    st.warning(
        "Dados simulados. Aplicação destinada "
        "exclusivamente a fins acadêmicos."
    )

    if st.button("Nova conversa"):
        st.session_state.mensagens = []
        st.session_state.sessao = criar_sessao()
        st.rerun()

if "agente" not in st.session_state:
    st.session_state.agente = criar_agente()

if "sessao" not in st.session_state:
    st.session_state.sessao = criar_sessao()

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

st.markdown("### Assistente de gestão hospitalar")

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

pergunta = st.chat_input(
    "Digite sua pergunta sobre o estoque hospitalar..."
)

if pergunta:
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        with st.spinner("Analisando o estoque..."):
            try:
                resposta = executar_agente(
                    st.session_state.agente,
                    pergunta,
                    st.session_state.sessao
                )

                st.markdown(resposta)

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": resposta
                })

            except Exception:
                st.error(
                    "Não foi possível processar a consulta. "
                    "Verifique a conexão e a configuração da API."
                )

st.divider()

st.caption(
    "StockMed AI | TP3 | "
    "Desenvolvimento de Data-Driven Apps com Python"
)