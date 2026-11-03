%%writefile relatorios.py
"""
Módulo responsável pela apresentação dos relatórios.
"""


def exibir_relatorio(titulo, **indicadores):
    """
    Exibe um relatório com título e indicadores.

    Args:
        titulo: Título do relatório.
        **indicadores: Pares de nome e valor dos indicadores.
    """
    print("\n" + "=" * 40)
    print(titulo)
    print("=" * 40)

    for nome, valor in indicadores.items():
        print(f"{nome}: {valor}")

    print("=" * 40)
