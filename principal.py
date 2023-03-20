from modelo.arquivo_entrada import ArquivoEntrada
from tradutor.relatorio_html import renderizar_template, escrever_relatorio_saida


# ler arquivo .csv e preencher objetos
objeto_arquivo_entrada = ArquivoEntrada()
objeto_arquivo_entrada.preencher_objeto_arquivo_entrada()

# renderizar template
template_renderizado = renderizar_template(objeto_arquivo_entrada)

# escrever relatorio
escrever_relatorio_saida(template_renderizado)



