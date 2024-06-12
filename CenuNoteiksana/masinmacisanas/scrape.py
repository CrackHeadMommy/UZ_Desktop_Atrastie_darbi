import requests
import os
from bs4 import BeautifulSoup as bs
import csv
import time


URL = "https://www.ss.lv/lv/transport/cars/today-5/sell/"
LAPAS = "lapas/"
DATI = "dati/"
MASINMACISANAS = "masinmacisanas/"

def saglaba(url, datne):
    rezultats = requests.get(url)
    print(rezultats.status_code)
    if rezultats.status_code == 200:
        with open(datne, 'w', encoding='utf-8') as fails:
            fails.write(rezultats.text)
    return

# saglaba(URL, LAPAS+"pirma.html")

def dabut_info(datne):
    dati = []
    with open(datne, "r", encoding="utf-8") as f:
        html = f.read()
    
    zupa = bs(html, 'html.parser')

    galvena_dala = zupa.find(id='page_main')

    tabulas = galvena_dala.find_all('table')

    rindas = tabulas[2].find_all('tr')
    for rinda in rindas[1:]: # Vai arī [1:-1] un tad jāizņem 36-38 rinda
        lauki = rinda.find_all('td')
        if len(lauki)<8:
            print('neatbilstošs datu skaits')
            continue
        auto = {}
        auto['sludinajuma_saite'] = lauki[1].find('a')['href']
        auto['bilde'] = lauki[1].find('img')['src']
        dati.append(auto)
    return dati


def saglaba_datus(dati):
    with open(MASINMACISANAS+DATI+"sslv.csv", "w", encoding='utf-8') as f:
        lauku_nosaukumi = ['sludinajuma_saite','bilde']
        w = csv.DictWriter(f, fieldnames= lauku_nosaukumi)
        w.writeheader()
        for auto in dati:
            w.writerow(auto)
    return


# saglaba_datus(dabut_info(LAPAS+"pirma.html"))


def atvilkt_lapas(skaits):
    for i in range(1,skaits+1):
        saglaba("{}page{}.html".format(URL, i), "{}lapa{}.html".format(LAPAS, i))
        time.sleep(1)
    return


def dabut_info_daudz(skaits):
    visi_dati = []
    for i in range(1, skaits+1):
        dati = dabut_info("{}lapa{}.html".format(LAPAS,i))
        visi_dati += dati
    return visi_dati

atvilkt_lapas(5)
info = dabut_info_daudz(5)
saglaba_datus(info)