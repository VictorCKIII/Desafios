
import shutil
import tabula
import pandas as pd

lista_tabela = tabula.read_pdf('Anexo_1.pdf', multiple_tables = True,  pages='all', encoding='utf-8', lattice=True)
                         

tabela = pd.concat(lista_tabela, ignore_index= True)

tabela = tabela.drop(columns=tabela.columns[tabela.columns.str.contains('^Unnamed')])

tabela.rename(columns={'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorial' }, inplace=True)

tabela.to_csv('tabelas_unidas.csv', index=False, encoding='utf-8-sig')


tabela_csv = 'tabelas_unidas.csv'

nome_zip = 'Teste_Victor.zip'
caminho_zip = shutil.make_archive(
    base_name= nome_zip,
    format='zip',
    root_dir='.',
    base_dir= tabela_csv
)








