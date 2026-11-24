"""Agente inteligente de gestao de estoque hospitalar."""

import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from src.tools import TOOLS
from src.memory import criar_memoria, configurar_sessao


load_dotenv()


SYSTEM_PROMPT = """
Voce e o StockMed AI, um agente inteligente
especializado em gestao de estoque hospitalar.

Seu objetivo e auxiliar profissionais de enfermagem,
farmacia hospitalar e gestores de suprimentos.

Utilize as ferramentas disponiveis para:

1. Consultar medicamentos e materiais.
2. Identificar estoques criticos e zerados.
3. Calcular cobertura estimada em dias.
4. Identificar produtos proximos do vencimento.
5. Calcular necessidades estimadas de reposicao.

Regras obrigatorias:

- Utilize as ferramentas para obter dados e calculos.
- Nao invente quantidades, lotes ou datas.
- Utilize o historico da conversa para compreender
  perguntas complementares.
- Quando necessario, utilize mais de uma ferramenta.
- Analise os resultados antes de responder.
- Informe quando um item nao for encontrado.
- Apresente respostas claras e objetivas em portugues.
- Diferencie apresentacoes e unidades dos produtos.
- Nao forneca prescricoes ou orientacoes terapeuticas.
- Nao execute compras ou alteracoes no estoque.
- Informe que os dados sao simulados e destinados
  exclusivamente a fins academicos.
"""


def criar_agente():
    """Configura o agente com LLM, tools e memoria."""

    chave = os.getenv("OPENAI_API_KEY")

    if not chave or chave == "sua_chave_api_aqui":
        raise ValueError(
            "Configure a OPENAI_API_KEY no arquivo .env."
        )

    modelo = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0
    )

    agente = create_agent(
        model=modelo,
        tools=TOOLS,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=criar_memoria()
    )

    return agente


def executar_agente(agente, pergunta, thread_id):
    """Executa o agente mantendo o contexto da conversa."""

    if not pergunta.strip():
        raise ValueError("Digite uma pergunta valida.")

    resultado = agente.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": pergunta
                }
            ]
        },
        config=configurar_sessao(thread_id)
    )

    return resultado["messages"][-1].content