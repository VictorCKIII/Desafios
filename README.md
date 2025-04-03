# Desafios Estágio

# Teste 1 - Web Scraping

- Esse teste é referente a branch *Web_Scraping*, onde é possível fazer a raspagem de dados do site que nos foi apresentado onde conseguimos fazer a buscar através das tags HTML e definir o que queremos pegar, com isso, conseguimos 'raspar' os links dos anexos presentes no site e com isso fazer o download e compactar os mesmos.

- Para visualizar melhor o funcionamento, exclua os arquivos *pdfs_baixados* e *pdfs_compactados* e rode o arquivo main.py . 

# Teste 2 - Transformação de Dados

- A branch *extrair* é referente a este teste de número 2, onde foi necessário pegar uma tabela com bastante dados e aplicar uma lógica atrelada a biblioteca *tabua* e *pandas* para que fosse capaz de ler o pdf *Anexo_1*, identificar e extrair todas as tabelas presentes neste pdf com o intuito de trazer as mesmas bem formatadas, juntar-las em um único arquivo e por fim, compactar este arquivo onde elas foram unidas.

- Para testar, basta excluir os arquivos *tabelas_unidas* e *Teste_Victor.zip* e executar o extrair.py .

# Teste 3 - Teste de Banco de Dados

- *Postgree* é a branch referente a este teste, onde na mesma podemos visualizar as consultas que foram feitas, tais as query criadas para que as consultas retornassem os resultados.

- Gostaria de fazer um adendo onde utilizei o Pgadmin 4 e nele tive o problema quando fui anexar as tabelas dos trimestres, pois os dados dos valores estavam com ',' e o Pgadmin4 trabalha apenas com '.', tentei de várias formas contornar esse problema, mas o único jeito que fui capaz de achar momentâneamente foi de transformar os campos das variáveis dos valores iniciais e finais em VARCHAR, para que eu pudesse anexar-los dentro do DB.


# Teste 4 - Teste de API

- *Api* é a branch que se refere a este teste. Lá, serão encontradas 2 pastas, *Servidor* e *Web*. O *Servidor* é onde está hospedada a API feita em Flask com a rota /buscar configurada para satisfazer as pesquisas mais relevantes da pesquisa, onde considera 2 colunas da tabela que foram as 'Razão Social e Modalidade', afim de preservar a integridade. Já na pasta *Web* é onde está a interface criada em Vue para se comunicar com a API, lá, contamos com um campo de busca para fazer as requisições que a API pode nos entregar. Também é possível encontrar a coleção feita no Postman na pasta *Servidor*. 

  
  
