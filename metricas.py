%%writefile metricas.py
"""
Módulo de cálculo de métricas de desempenho.

Contém funções reutilizáveis para calcular médias,
taxas de cumprimento de metas e resumos de indicadores.
"""


def calcular_media(*valores):
    """
    Calcula a média aritmética de valores numéricos.

    Args:
        *valores: Quantidade variável de números.

    Returns:
        float: Média dos valores informados.

    Raises:
        ValueError: Se nenhum valor for informado.
    """
    if not valores:
        raise ValueError("Informe pelo menos um valor.")

    return sum(valores) / len(valores)


def calcular_taxa_cumprimento(realizado, meta=100):
    """
    Calcula o percentual de cumprimento de uma meta.

    Args:
        realizado: Resultado efetivamente alcançado.
        meta: Meta estabelecida (padrão: 100).

    Returns:
        float: Percentual de cumprimento da meta.

    Raises:
        ValueError: Se a meta for zero ou negativa.
    """
    if meta <= 0:
        raise ValueError("A meta deve ser maior que zero.")

    return (realizado / meta) * 100


def classificar_desempenho(taxa, limite=100):
    """
    Classifica o desempenho conforme a taxa alcançada.

    Args:
        taxa: Percentual de cumprimento.
        limite: Percentual mínimo para atingir a meta.

    Returns:
        str: Classificação do desempenho.
    """
    if taxa >= limite:
        return "Meta atingida"
    return "Meta não atingida"


def criar_resumo(**metricas):
    """
    Organiza métricas recebidas como argumentos nomeados.

    Args:
        **metricas: Indicadores no formato nome=valor.

    Returns:
        dict: Dicionário com os indicadores recebidos.
    """
    return dict(metricas)


def demonstrar_escopo():
    """
    Demonstra uma variável local e uma variável global.
    """
    mensagem_local = "Esta variável existe nesta função."
    return mensagem_local


# Variável global do módulo
sistema = "Análise de Desempenho"
