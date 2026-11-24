from src.tools import (
    consultar_estoque,
    identificar_estoque_critico,
    calcular_cobertura,
    verificar_validade,
    calcular_reposicao,
)


def test_consultar_estoque():
    resultado = consultar_estoque.invoke(
        {"nome": "Ribociclibe"}
    )
    assert "Ribociclibe" in resultado
    assert "12" in resultado


def test_identificar_estoque_critico():
    resultado = identificar_estoque_critico.invoke({})
    assert "Ribociclibe" in resultado
    assert "Epcoritamabe" in resultado


def test_calcular_cobertura():
    resultado = calcular_cobertura.invoke(
        {"nome": "Ribociclibe"}
    )
    assert "4" in resultado
    assert "dias" in resultado.lower()


def test_verificar_validade():
    resultado = verificar_validade.invoke(
        {"dias": 30}
    )
    assert isinstance(resultado, str)
    assert "erro" not in resultado.lower()


def test_calcular_reposicao():
    resultado = calcular_reposicao.invoke(
        {"nome": "Ribociclibe"}
    )
    assert "78" in resultado


def test_medicamento_inexistente():
    resultado = consultar_estoque.invoke(
        {"nome": "MedicamentoXYZ"}
    )
    assert "encontrad" in resultado.lower()