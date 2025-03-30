
import requests 
from bs4 import BeautifulSoup

pagina = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')

dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

anexos = dados_pagina.find_all('div', id="cfec435d-6921-461f-b85a-b425bc3cb4a5")

links_to_download = []


def retorna_links():

    for div in anexos:

        pequisa_ol = div.find('ol')
        pesquisa_li = pequisa_ol.find_all('li')
        pesquisa_lista1 = pesquisa_li[0]
        link_pesquisa1 = pesquisa_lista1.find('a')
        link_tag = link_pesquisa1['href']
        print('----------------------------------------------')
        print('Link 1 ---->  ' +  link_tag )
        print('----------------------------------------------')
        

        pesquisa_lista2 = pesquisa_li[1]
        link_pesquisa2 = pesquisa_lista2.find('a')
        link_tag2 = link_pesquisa2['href']
        print( 'Link 2 ---->  ' + link_tag2)
        print('----------------------------------------------')

    links_to_download.append(link_tag)
    links_to_download.append(link_tag2)

     
    return links_to_download
   
    