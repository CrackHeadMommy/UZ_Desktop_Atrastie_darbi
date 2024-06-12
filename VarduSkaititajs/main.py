import requests as rq

rezultats = rq.get('http://universities.hipolabs.com/search?country=Latvia')

dati = rezultats.json()


sakartoti_dati = sorted(dati, key=lambda x: x["name"])

for viens in sakartoti_dati:
    print(viens["name"])


