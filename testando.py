import requests
import sys
from bs4 import BeautifulSoup

webSites = [
    ['portaldomedico', 'equipaments', 'https://www.portaldomedico.com/Busca/Index?busca=', 'cartaoProdutoTitulo', 'cartaoProdutoTitulo', 'cartaoProdutoValor'],
    ['ebay', 'equipaments', 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.Xstethoscope.TRS0&_nkw=', 'sresult ', 'lvtitle', 'lvprice prc']
]


def clear():
    i = 0
    for i in range(0, 100):
        print('\n')
        i = i+1


def define_parameters(target):
    if target == 1:
        web_site = input("Em qual site deseja buscar? pressione ENTER para ver a lista de websites\n")
        if web_site == '':
            num = len(webSites)
            while num > 0:
                print(webSites[num-1][0])
                num = num - 1
            web_site = input("Em qual site deseja buscar?\n")
        product = input("Qual o nome do equipamento medico?\n")
    if target == 2:
        web_site = input("Em qual site deseja buscar? pressione ENTER para ver a lista de websites\n")
        product = input("Qual o nome do remedio?\n")
    return choice_website(web_site, product)


def choice_website(sitename, query):
    num = len(webSites)
    while num > 0:
        if webSites[num - 1][0] == sitename:
            request = requests.get(webSites[num - 1][2] + query)
            site_html = BeautifulSoup(request.content, 'html.parser')

            cont = str(site_html).count(webSites[num-1][3])
            print("Foram encontrados", cont, "resultados para \"", query, "\"\n")
            for cont in range(0, cont):
                print("nome do produto:", site_html.find_all(class_ = webSites[num-1][4])[cont].get_text())
                print("preco:", site_html.find_all(class_ = webSites[num-1][5])[cont].get_text())
                cont = cont-1

            return input("\nPresione qualquer tecla para voltar ao menu\n"), clear(), principal_menu()
            break

        else:
            if num == 1:
                return clear(), print("Site nao cadastrado"), principal_menu()
        num = num - 1


def about():
    print("Authors:\n\nVictor H. Nogueira - GitHub: @victorhnog\nMarianne Anjos - GitHub: @anjossmarianne\nLuiz E. Sonoda - GitHub: @luizsonoda\nLuiz H. Rezende - GitHub: @lhenriquerezende")
    return input("\nPresione qualquer tecla para voltar ao menu\n"), clear(), principal_menu()


def principal_menu():
    buy_type = int(input('MENU\n1 - Comprar equipamentos medicos\n2 - Comprar remedios\n3 - Sobre\n4 - sair\n'))

    if buy_type == 1 or buy_type == 2:
        return clear(), define_parameters(buy_type)
    else:
        if buy_type == 3:
            return clear(), about()
        else:
            if buy_type == 4:
                return sys.exit()
            else:
                return clear(), print("Invalido, entre com outro valor\n"), principal_menu()

# Execution

principal_menu()
