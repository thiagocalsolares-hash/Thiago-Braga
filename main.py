"""
Script principal do sistema de análise de desempenho.
"""

from metricas import (
    calcular_media,
    calcular_taxa_cumprimento,
    classificar_desempenho,
    criar_resumo,
    demonstrar_escopo,
    sistema
)

from relatorios import exibir_relatorio


def main():
    """Executa a análise das métricas de desempenho."""

    # Dados de exemplo: produtividade semanal
    produtividade = [80, 90, 100, 85, 95]

    # Chamada com argumentos posicionais usando *
    media = calcular_media(*produtividade)

    # Argumentos posicionais e valor padrão
    taxa = calcular_taxa_cumprimento(media)

    # Argumento nomeado para alterar o limite padrão
    classificacao = classificar_desempenho(
        taxa, limite=90
    )

    # Criação de um resumo usando argumentos nomeados
    indicadores = criar_resumo(
        produtividade_media=round(media, 2),
        taxa_cumprimento=f"{taxa:.2f}%",
        classificacao=classificacao
    )

    # Apresentação do relatório
    exibir_relatorio(
        sistema,
        **indicadores
    )

    # Demonstração de retorno e escopo
    print(demonstrar_escopo())


if __name__ == "__main__":
    main()
