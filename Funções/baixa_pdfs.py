import requests
import os

pasta_downloads = "pdfs_baixados"
os.makedirs(pasta_downloads, exist_ok=True)

def baixa_pdf (links_to_download):


    for i, link in enumerate(links_to_download):
        try:
            response = requests.get(link, stream=True)
            if response.status_code == 200:
                nome_arquivo = f"{pasta_downloads}/Anexo_{i+1}.pdf"
                
                with open(nome_arquivo, "wb") as f:
                    f.write(response.content)
                
                print(f"✅ Download concluído: {nome_arquivo}")
            else:
                print(f"❌ Erro ao baixar {link} - Código {response.status_code}")
        except Exception as e:
            print(f"❌ Erro ao baixar {link}: {e}")

    print("📂 Todos os downloads foram concluídos!")  