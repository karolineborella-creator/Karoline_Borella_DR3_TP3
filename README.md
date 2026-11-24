# StockMed AI — Agente Inteligente de Gestão de Estoque Hospitalar

## 1. Identificação acadêmica

- Aluna: Karoline Alvellos Borella
- Instituição: Instituto Infnet
- Disciplina: Desenvolvimento de Data-Driven Apps com Python
- Atividade: TP3
- Ano: 2026

## 2. Contextualização do problema

A gestão de medicamentos e materiais hospitalares exige monitoramento contínuo dos níveis de estoque, consumo, validade e necessidade de reposição.

A ausência de ferramentas eficientes de monitoramento pode contribuir para desabastecimento, desperdício de recursos e dificuldades no planejamento logístico.

O StockMed AI foi desenvolvido como uma solução acadêmica baseada em inteligência artificial para auxiliar nesse processo.

## 3. Objetivo

Desenvolver um agente inteligente utilizando modelos de linguagem de grande porte (LLMs), integrado a ferramentas computacionais e memória conversacional, capaz de responder perguntas sobre o estoque hospitalar em linguagem natural.

## 4. Tecnologias utilizadas

- Python
- LangChain
- LangGraph
- OpenAI API
- GPT-4o-mini
- Pandas
- Streamlit
- Python-dotenv
- Pytest
- Git e GitHub

## 5. Base de dados

O projeto utiliza o arquivo data/estoque.csv, contendo dados simulados de medicamentos e materiais hospitalares.

Características da base:

- 50 registros.
- 12 colunas.
- Nenhum valor ausente identificado.
- Nenhum identificador duplicado identificado.

Os dados são fictícios e destinados exclusivamente a fins acadêmicos.

## 6. Funcionalidades

O agente disponibiliza cinco ferramentas:

| Ferramenta | Finalidade |
|---|---|
| consultar_estoque | Consultar medicamentos e materiais cadastrados. |
| identificar_estoque_critico | Identificar itens abaixo do estoque mínimo. |
| calcular_cobertura | Estimar os dias de cobertura do estoque. |
| verificar_validade | Identificar itens próximos ao vencimento. |
| calcular_reposicao | Estimar a quantidade necessária para reposição. |

O sistema também possui memória conversacional, permitindo perguntas subsequentes relacionadas ao contexto anterior.

## 7. Arquitetura da solução

Fluxo de funcionamento:

Usuário → Streamlit → Agente LangChain/LangGraph → LLM → Ferramentas Python → Base CSV → Resposta ao usuário.

A memória conversacional mantém o contexto da sessão, permitindo a continuidade das interações.

Os cálculos e consultas são realizados pelas ferramentas Python, reduzindo a dependência de cálculos produzidos diretamente pelo modelo de linguagem.

## 8. Estrutura do projeto

    Karoline_Borella_DR3_TP3/
    ├── data/
    │   └── estoque.csv
    ├── docs/
    │   └── evidencias/
    ├── src/
    │   ├── __init__.py
    │   ├── agent.py
    │   ├── memory.py
    │   └── tools.py
    ├── tests/
    │   └── test_tools.py
    ├── .env.example
    ├── .gitignore
    ├── app.py
    ├── README.md
    └── requirements.txt

## 9. Instalação e configuração

Criar o ambiente virtual:

    python -m venv .venv

Ativar o ambiente virtual no Windows:

    .\.venv\Scripts\Activate.ps1

Instalar as dependências:

    python -m pip install -r requirements.txt

Criar um arquivo .env a partir do modelo .env.example e configurar:

    OPENAI_API_KEY=sua_chave_api
    OPENAI_MODEL=gpt-4o-mini

A chave real da API não deve ser compartilhada ou publicada no GitHub.

## 10. Execução da aplicação

Executar no terminal:

    python -m streamlit run app.py

Acessar no navegador:

    http://localhost:8501

## 11. Exemplos de utilização

- Qual é o estoque de Ribociclibe?
- Quantos dias de cobertura temos desse medicamento?
- Quais itens apresentam estoque crítico?
- Quais produtos vencerão nos próximos 30 dias?
- Qual quantidade de Ribociclibe precisa ser reposta?

## 12. Validação e testes automatizados

Executar:

    python -m pytest tests/test_tools.py -v

Resultados observados:

- Testes executados: 6.
- Testes aprovados: 6.
- Testes reprovados: 0.
- Taxa de aprovação: 100%.
- Tempo registrado na execução inicial: 3,51 segundos.

Foram testadas as cinco ferramentas e uma consulta envolvendo medicamento inexistente.

Também foram realizados testes funcionais do agente e da memória conversacional por meio da interface Streamlit.

As evidências encontram-se na pasta docs/evidencias.

## 13. Resultados obtidos

Durante os testes com dados simulados, o agente apresentou os seguintes resultados para o Ribociclibe 200 mg:

- Estoque disponível: 12 comprimidos.
- Estoque mínimo: 30 comprimidos.
- Cobertura estimada: 4 dias.
- Reposição estimada: 78 comprimidos.

O agente identificou corretamente a condição de estoque abaixo do mínimo e demonstrou capacidade de manter o contexto entre perguntas consecutivas.

## 14. Segurança e limitações

- Utilização exclusiva de dados simulados.
- Proteção da chave da API por variáveis de ambiente.
- Exclusão de credenciais do controle de versão.
- Dependência de conexão com a internet e disponibilidade da API.
- Possibilidade de respostas imprecisas do modelo de linguagem.
- Necessidade de validação humana dos resultados.
- Aplicação acadêmica, sem validação para uso assistencial ou operacional real.

## 15. Possibilidades de evolução

- Integração com bancos de dados relacionais.
- Desenvolvimento de dashboards gerenciais.
- Implementação de alertas automatizados.
- Previsão de demanda.
- Controle de acesso por perfil de usuário.
- Integração com sistemas de gestão hospitalar.

## 16. Conclusão

O StockMed AI demonstra a aplicação de agentes inteligentes baseados em LLMs na gestão de estoque hospitalar.

A integração entre ferramentas computacionais, memória conversacional e interface interativa permite realizar consultas e análises em linguagem natural.

Os testes realizados demonstraram o funcionamento das funcionalidades implementadas no cenário acadêmico proposto.

## 17. Referências

- Python: https://docs.python.org/
- LangChain: https://docs.langchain.com/
- LangGraph: https://docs.langchain.com/
- OpenAI: https://platform.openai.com/docs/
- Streamlit: https://docs.streamlit.io/
- Pandas: https://pandas.pydata.org/docs/
- Pytest: https://docs.pytest.org/

## 18. Declaração de uso de inteligência artificial

O ChatGPT, da OpenAI, foi utilizado como ferramenta de apoio ao desenvolvimento, à elaboração de código, à documentação e à orientação dos testes.

Os procedimentos de execução e os resultados apresentados foram verificados no ambiente de desenvolvimento do projeto.