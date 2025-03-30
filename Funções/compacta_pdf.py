import shutil


def compacta():
    pdf_zip = "pdfs_compactados.zip"


    pasta_downloads = "pdfs_baixados"


    shutil.make_archive(pdf_zip.replace(".zip", ""), 'zip', pasta_downloads)

    print(f"✅ Arquivos compactados em {pdf_zip}")
