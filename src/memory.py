"""Gerenciamento da memoria conversacional do StockMed AI."""

from uuid import uuid4
from langgraph.checkpoint.memory import InMemorySaver


def criar_memoria():
    """Cria o armazenamento do historico conversacional."""
    return InMemorySaver()


def criar_sessao():
    """Gera um identificador exclusivo para cada conversa."""
    return str(uuid4())


def configurar_sessao(thread_id: str):
    """Configura a identificacao da conversa do agente."""
    return {
        "configurable": {
            "thread_id": thread_id
        },
        "recursion_limit": 50
    }