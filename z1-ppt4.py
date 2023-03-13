from datetime import datetime
import webbrowser
import requests

pageurl = input("Podaj adres url: ")
for x in range(3):
    date = (datetime.today()).replace(year=datetime.today().year-(x+1)).strftime('%Y%m%d')
    url = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date)
    response = requests.get(url)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    print("Wersja sprzed lat : " + str(x+1) + " : " + page)
    webbrowser.open(page)

