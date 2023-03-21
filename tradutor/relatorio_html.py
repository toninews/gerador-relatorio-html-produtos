from jinja2 import Template
from utilitarios.utils import remover_caracter_transformar_inteiro

def ler_template_html():
    arquivo_template = open('templates/template.html', 'r')
    arquivo_texto = arquivo_template.read()
    arquivo_template.close()
    return arquivo_texto

def renderizar_template(objeto_arquivo_entrada):
    arquivo_texto = ler_template_html()
    template = Template(arquivo_texto)

    precos = criar_lista_precos_produtos(objeto_arquivo_entrada.produtos)
    dicionario_precos_agrupado_por_marca = calcular_media_preco_por_marca(objeto_arquivo_entrada.produtos)
    template_renderizado = template.render(cabecalho=objeto_arquivo_entrada.cabecalho,
                                           produtos=objeto_arquivo_entrada.produtos,
                                           total_produtos=len(objeto_arquivo_entrada.produtos),
                                           produto_mais_barato=min(precos),
                                           produto_mais_caro=max(precos),
                                           dicionario_media_preco_por_marca=dicionario_precos_agrupado_por_marca)
    return template_renderizado

def criar_lista_precos_produtos(produtos):
    precos = []

    for produto in produtos:
        valor_formatado = remover_caracter_transformar_inteiro(produto.preco)
        precos.append(valor_formatado)

    return precos

def agrupar_precos_por_marca(produtos):
    dicionario_precos_agrupado_por_marca = {}

    for produto in produtos:
        valor_formatado = remover_caracter_transformar_inteiro(produto.preco)
        if produto.marca not in dicionario_precos_agrupado_por_marca:
            dicionario_precos_agrupado_por_marca[produto.marca] = [valor_formatado]
        else:
            dicionario_precos_agrupado_por_marca[produto.marca].append(valor_formatado)

    return dicionario_precos_agrupado_por_marca

def calcular_media_preco_por_marca(produtos):
    dicionario_precos_agrupado_por_marca = agrupar_precos_por_marca(produtos)

    for marca in dicionario_precos_agrupado_por_marca:
        lista_precos = dicionario_precos_agrupado_por_marca[marca]
        media = sum(lista_precos) / len(lista_precos)
        dicionario_precos_agrupado_por_marca[marca] = int(media)

    return dicionario_precos_agrupado_por_marca

def escrever_relatorio_saida(template_renderizado):
    with open('templates/relatorio_gerado.html', 'w') as arquivo_saida:
        arquivo_saida.write(template_renderizado)