# Covid DF Scraper
Este repositório contém o código para raspagem de dados dos Boletins Covid-19 divulgados pelo Governo do Distrito Federal (GDF). O código acessa a html da divulgação dos boletins epidemiológicos diários, coleta os links dos boletins, agrupa os informes, datas e links e cria uma tabela csv com os dados coletados automaticamente. Apenas para os dados divulgados em 2021. O projeto pode ser adaptado para outros sites que divulguem informações que necessitem ser baixados periodicamente.

# Metodologia
Programa que executa processo ETL - Extract, Transform, Load:
- EXTRACT: acessa site o site da Secretaria de Saúde do DF, identifica e extrai do HTML apenas dados de interesse 
- TRASNFORM: limpeza de dados e seleção do número do informe e do link dos boletins epidemiológicos
- LOAD: salva os dados extraídos em uma planilha csv

**Bibliotecas usadas:** pandas, requests e BeautifulSoup
**Método:** baixa código HTML, localiza links pela única `tag <div id="conteudo">`, localiza `tags-children p`, para então localizar "Informativo" e criar a variável `data`. Depois, localizar o "Informe nº", para raspar os dados e criar as variáveis `numero_informe` e `link`. Verificou-se em tags `a` com atributos `href` palavras que não foram totalmente linkadas. Por isso, foi necessário localizar algumas variáveis `numero_informe` e `link `pela palavra cortada "nforme nº". Em outros casos, foi verificado que não havia a palavra "Informativo" para localizar uma data, sendo necessário localizar pela expressão "tese diária de óbitos". Depois das correções, foi usado um dicionário com chaves de meses por extenso, com valores dos meses numéricos para padronizar a data apenas com números. Depois, foi criado um dicionário e arquivo csv, com colunas com data de publicação, número do informe e link que leva para o download do arquivo em pdf, divulgado pela Secretaria de Saúde do DF. Apenas links de 2021.

# Fonte das informações
Os boletins epidemiológicos são produzidos diariamente pela Diretoria de Vigilância Epidemiológica da Subsecretaria de Vigilância à Saúde da Secretaria de Saúde do Distrito Federal. A divulgação é feita pelo site: https://www.saude.df.gov.br/boletinsinformativos-divep-cieves.

# Dicionário

|         Variável       |      Definição        |
|------------------------|-------------------------------|
|url|endereço do site a ser raspado|
|html|html já codificado|
|tags_p|Lista de objetos contidos na tag `<p>`|
|data|Lista com datas de divulgação dos boletins|
|numero_informe| Número do boletim|
|link|Lista de links correspondentes a cada informe|
|registros|Dicionário com chaves: data, número_informe e link|


# Autoria
Carina Dourado 

# Sobre
Trabalho final do Master em Jornalismo de Dados, Automação e Data Storytelling, do Insper, das disciplinas
- Pensamento Computacional - professor: [Álvaro Justen (Turicas)](https://github.com/turicas)
- Transparência, reprodutibilidade e uso ético de dados - professoras: [Natália Mazotte](https://github.com/ncortezrj) e [Carla Vieira](https://github.com/carlaprv) 

# Manutenção
Última atualização: 18/10/2021
