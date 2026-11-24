"""Ferramentas de gestao de estoque do StockMed AI."""

from pathlib import Path
from datetime import date
import unicodedata

import pandas as pd
from langchain_core.tools import tool


# Caminho da base de dados
BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_ESTOQUE = BASE_DIR / "data" / "estoque.csv"


def carregar_estoque():
    """Carrega a base de estoque hospitalar simulada."""
    df = pd.read_csv(ARQUIVO_ESTOQUE)
    df["data_validade"] = pd.to_datetime(
        df["data_validade"], errors="raise"
    )
    return df


def normalizar(texto):
    """Remove acentos e padroniza textos para busca."""
    texto = unicodedata.normalize("NFKD", str(texto))
    return "".join(
        c for c in texto
        if not unicodedata.combining(c)
    ).lower().strip()


def buscar_item(df, nome):
    """Localiza itens pelo nome ou apresentacao."""
    termo = normalizar(nome)

    if not termo:
        raise ValueError("Informe o nome do item.")

    textos = (
        df["nome_item"] + " " + df["apresentacao"]
    ).apply(normalizar)

    return df[textos.str.contains(termo, regex=False)].copy()


@tool
def consultar_estoque(nome: str) -> str:
    """Consulta quantidade, apresentacao, lote e validade de um item."""
    try:
        df = carregar_estoque()
        resultado = buscar_item(df, nome)

        if resultado.empty:
            return f"Item '{nome}' nao encontrado."

        colunas = [
            "nome_item",
            "apresentacao",
            "unidade_medida",
            "lote",
            "quantidade_disponivel",
            "estoque_minimo",
            "data_validade",
        ]

        return resultado[colunas].to_string(index=False)

    except Exception as erro:
        return f"Erro na consulta: {erro}"


@tool
def identificar_estoque_critico() -> str:
    """Identifica itens abaixo do estoque minimo, incluindo zerados."""
    try:
        df = carregar_estoque()

        criticos = df[
            df["quantidade_disponivel"] < df["estoque_minimo"]
        ].copy()

        if criticos.empty:
            return "Nenhum item em estoque critico."

        criticos = criticos.sort_values(
            "quantidade_disponivel"
        )

        colunas = [
            "nome_item",
            "apresentacao",
            "quantidade_disponivel",
            "estoque_minimo",
        ]

        return (
            f"Total de itens criticos: {len(criticos)}\n"
            + criticos[colunas].to_string(index=False)
        )

    except Exception as erro:
        return f"Erro na analise: {erro}"


@tool
def calcular_cobertura(nome: str) -> str:
    """Calcula a cobertura estimada de estoque em dias."""
    try:
        df = carregar_estoque()
        itens = buscar_item(df, nome)

        if itens.empty:
            return f"Item '{nome}' nao encontrado."

        respostas = []

        for _, item in itens.iterrows():
            quantidade = item["quantidade_disponivel"]
            consumo = item["consumo_medio_diario"]

            identificacao = (
                f"{item['nome_item']} "
                f"{item['apresentacao']}"
            )

            if item["data_validade"].date() < date.today():
                respostas.append(
                    f"{identificacao}: lote vencido."
                )
            elif consumo <= 0:
                respostas.append(
                    f"{identificacao}: consumo insuficiente "
                    "para calcular cobertura."
                )
            else:
                cobertura = quantidade / consumo

                respostas.append(
                    f"{identificacao}: "
                    f"{cobertura:.2f} dias de cobertura estimada."
                )

        return "\n".join(respostas)

    except Exception as erro:
        return f"Erro no calculo de cobertura: {erro}"


@tool
def verificar_validade(dias: int = 30) -> str:
    """Identifica itens vencidos e a vencer no periodo informado."""
    try:
        if dias < 0:
            return "Informe um periodo maior ou igual a zero."

        df = carregar_estoque()
        hoje = pd.Timestamp(date.today())

        df["dias_para_vencer"] = (
            df["data_validade"] - hoje
        ).dt.days

        resultado = df[
            (df["dias_para_vencer"] <= dias)
            & (df["quantidade_disponivel"] > 0)
        ].copy()

        if resultado.empty:
            return "Nenhum item vencido ou a vencer no periodo."

        resultado["situacao"] = resultado[
            "dias_para_vencer"
        ].apply(
            lambda x: "Vencido" if x < 0 else "A vencer"
        )

        resultado = resultado.sort_values(
            "dias_para_vencer"
        )

        colunas = [
            "nome_item",
            "apresentacao",
            "lote",
            "quantidade_disponivel",
            "data_validade",
            "dias_para_vencer",
            "situacao",
        ]

        return (
            f"Data de referencia: {hoje.date()}\n"
            f"Total de itens: {len(resultado)}\n"
            + resultado[colunas].to_string(index=False)
        )

    except Exception as erro:
        return f"Erro na verificacao de validade: {erro}"


@tool
def calcular_reposicao(nome: str) -> str:
    """Calcula a reposicao estimada para atingir o estoque alvo."""
    try:
        df = carregar_estoque()
        itens = buscar_item(df, nome)

        if itens.empty:
            return f"Item '{nome}' nao encontrado."

        respostas = []

        for _, item in itens.iterrows():
            disponivel = item["quantidade_disponivel"]
            alvo = item["estoque_alvo"]

            if item["data_validade"].date() < date.today():
                disponivel = 0

            reposicao = max(0, alvo - disponivel)

            respostas.append(
                f"{item['nome_item']} "
                f"{item['apresentacao']}: "
                f"reposicao estimada de {reposicao} "
                f"({item['unidade_medida']})."
            )

        return "\n".join(respostas)

    except Exception as erro:
        return f"Erro no calculo de reposicao: {erro}"


# Ferramentas disponibilizadas ao agente LangChain
TOOLS = [
    consultar_estoque,
    identificar_estoque_critico,
    calcular_cobertura,
    verificar_validade,
    calcular_reposicao,
]