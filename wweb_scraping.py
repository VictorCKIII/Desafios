import requests 
from bs4 import BeautifulSoup
import os
import shutil
from Funções import retorna_links
from Funções import baixa_pdfs
from Funções import compacta_pdf

# pagina = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')

# dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

# anexos = dados_pagina.find_all('div', id="cfec435d-6921-461f-b85a-b425bc3cb4a5")


# links_to_download = []

# def retorna_link ():

#     for div in anexos:

#         pequisa_ol = div.find('ol')
#         pesquisa_li = pequisa_ol.find_all('li')
#         pesquisa_lista1 = pesquisa_li[0]
#         link_pesquisa1 = pesquisa_lista1.find('a')
#         link_tag = link_pesquisa1['href']
#         print('----------------------------------------------')
#         print('Link 1 ---->  ' +  link_tag )
#         print('----------------------------------------------')
        

#         pesquisa_lista2 = pesquisa_li[1]
#         link_pesquisa2 = pesquisa_lista2.find('a')
#         link_tag2 = link_pesquisa2['href']
#         print( 'Link 2 ---->  ' + link_tag2)
#         print('----------------------------------------------')

#     links_to_download.append(link_tag)
#     links_to_download.append(link_tag2)

# retorna_link()

varTeste = retorna_links.retorna_links()

baixa_pdfs.baixa_pdf(varTeste)

compacta_pdf.compacta()

# pasta_downloads = "pdfs_baixados"
# os.makedirs(pasta_downloads, exist_ok=True)

# for i, link in enumerate(links_to_download):
#     try:
#         response = requests.get(link, stream=True)
#         if response.status_code == 200:
#             nome_arquivo = f"{pasta_downloads}/Anexo_{i+1}.pdf"
            
#             with open(nome_arquivo, "wb") as f:
#                 f.write(response.content)
            
#             print(f"✅ Download concluído: {nome_arquivo}")
#         else:
#             print(f"❌ Erro ao baixar {link} - Código {response.status_code}")
#     except Exception as e:
#         print(f"❌ Erro ao baixar {link}: {e}")

# print("📂 Todos os downloads foram concluídos!")  


# pdf_zip = "pdfs_compactados.zip"

# # Pasta onde estão os PDFs
# pasta_downloads = "pdfs_baixados"

# # Criar o ZIP com todos os PDFs
# shutil.make_archive(pdf_zip.replace(".zip", ""), 'zip', pasta_downloads)

# print(f"✅ Arquivos compactados em {pdf_zip}")

   




    