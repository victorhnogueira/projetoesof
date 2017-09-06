import requests
from bs4 import BeautifulSoup


def clear():
    i = 0
    for i in range(0, 100):
        print('\n')
        i = i+1


webSites = [
    ['portalmedico', 'https://www.portaldomedico.com/Busca/Index?busca=', 'cartaoProdutoTitulo', 'cartaoProdutoValor'],
    ['centermedical', 'http://www.centermedical.com.br/', 'cartaoProdutoTitulo', 'cartaoProdutoValor']

]


def define_parameters(target):
    if target == 1:
        web_site = input("Em qual site deseja buscar? precione ENTER para ver a lista de websites\n")
        product = input("Qual o nome do medicamento?\n")
    if target == 2:
        web_site = input("Em qual site deseja buscar?\n")
        product = input("Qual o nome do equipamento medico?\n")
    return find_products(web_site, product)


def find_products(site_target, query):
    request = requests.get(site_target+query)
    site_html = BeautifulSoup(request.content, 'html.parser')
    return print(site_html)


def about():
    print("Authors:\n\nVictor H. Nogueira - GitHub: @victorhnog\nMarianne Anjos - GitHub: @anjossmarianne\nLuiz E. Sonoda - GitHub: @luizsonoda\nLuiz H. Rezende - GitHub: @lhenriquerezende")
    return input("\nPresione qualquer tecla para voltar ao menu\n"), clear(), principal_menu()


def principal_menu():
    buy_type = int(input('O que voce deseja comprar?\n1 - Remedios\n2 - Equipamentos medicos\n3 - Sobre\n'))
    if buy_type == 1 or buy_type == 2:
        return clear(), define_parameters(buy_type)
    else:
        if buy_type == 3:
            return clear(), about()
        else:
            return clear(), print("Invalido, entre com outro valor\n"), principal_menu()

# Execution

principal_menu()
