import csv
import requests
from bs4 import BeautifulSoup

url = 'http://www.wtatennis.com/singles-rankings'
page = requests.get(url)
soup = BeautifulSoup(page.content)

cells = [s.get_text().strip().encode("utf-8") for s in soup.select("#myTable td")]

with open('wta.csv', 'wb') as csvfile:
    wtawriter = csv.writer(csvfile)
    for i in range(0, 101):
        wtawriter.writerow(cells[i*7:i*7+7])
