import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.saude.df.gov.br/boletinsinformativos-divep-cieves/"
resposta = requests.get(url)  
html = resposta.text 
soup = BeautifulSoup(html, "html.parser")
registros = []
div = soup.find("div", {"id": "conteudo"})
data = numero_informe = link = None
tags_p = div.findChildren("p")
for tag_p in tags_p:
    if "Informativo" in tag_p.text and "do dia" in tag_p.text:
        if data is not None and numero_informe is not None and link is not None:
            registros.append({"data": data, "numero": numero_informe, "link": link})
            data = numero_informe = link = None
        data = tag_p.text.split("do dia ")[1].replace(" de 2021", "").replace("º", "").strip()
    elif "nforme nº" in tag_p.text:
        numero_informe = tag_p.text.split("nº")[1].strip()
        link = tag_p.findChildren("a")[0]["href"]
    elif "tese diária de óbitos" in tag_p.text:
        data = tag_p.text.split(" em ")[1].replace(" de 2021", "").replace("º", "").strip()
        data = data.split()
        data_num = {"janeiro":"1", "fevereiro":"2", "março":"3", "abril":"4", 
                    "maio":"5", "junho":"6","julho":"7", "agosto":"8", 
                    "setembro":"9", "outubro":"10", "novembro":"11", "dezembro":"12"}
        for mes_numero in data:
          if data[2] == "janeiro":
            mes_numero = "1"
          elif data[2] == "fevereiro" :
            mes_numero = "2"
          elif data[2] == "março":
            mes_numero = "3"
          elif data[2] == "abril":
            mes_numero = "4"
          elif data[2] == "maio":
            mes_numero = "5"
          elif data[2] == "junho":
            mes_numero = "6"
          elif data[2] == "julho":
            mes_numero = "7"
          elif data[2] == "agosto":
            mes_numero = "8"
          elif data[2] == "setembro":
            mes_numero = "9"
          elif data[2] == "outubro":
            mes_numero = "10" 
          elif data[2] == "novembro":
            mes_numero == "11"
          elif data[2] == "dezembro":
            mes_numero = "12"
        data = (f"{data[0]}/{mes_numero}/21")
if data is not None and numero_informe is not None and link is not None:
    registros.append({"data": data, "numero": numero_informe, "link": link})
    df = pd.DataFrame(registros)
    df.to_csv('boletins_covid.csv') 
