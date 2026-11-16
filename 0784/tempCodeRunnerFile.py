def relatorio(titulo, *linhas, rodape="Fim"):
    print(titulo)
    for linha in linhas:
        print("-", linha)
    print(rodape)

relatorio("Relatório Semanal", "Vendas subiram", "Stock ok")
relatorio("Relatório Final", "Tudo concluído", rodape="Assinado: Gestão")