import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.saude.df.gov.br/boletinsinformativos-divep-cieves/"
meses = {"janeiro":"01",
         "fevereiro":"02",
         "março":"03",
         "abril":"04",
         "maio":"05",
         "junho":"06",
         "julho":"07",
         "agosto":"08",
         "setembro":"09",
         "outubro":"10",
         "novembro":"11",
         "dezembro":"12"}
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
        mes_numero = meses[data[2]]
        data = (f"{data[0]}/{mes_numero}/21")
if data is not None and numero_informe is not None and link is not None:
    registros.append({"data": data, "numero": numero_informe, "link": link})
    df = pd.DataFrame(registros)
    df.to_csv('boletins_covid.csv')
