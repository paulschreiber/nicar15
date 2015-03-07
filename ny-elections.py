import requests
from bs4 import BeautifulSoup

url = 'http://www.elections.ny.gov/CountyBoards.html'
page = requests.get(url)
soup = BeautifulSoup(page.content)

# get the county URLs from the <area> tags
counties = soup.select("area")
county_urls = [u.get('href') for u in counties]

# skip dummy URL
county_urls = county_urls[1:]

# remove duplicates
county_urls = list(set(county_urls))

# store results here
data = []

for url in county_urls:
    print "Fetching %s" % url
    page = requests.get(url)
    soup = BeautifulSoup(page.content)
    lines = [s for s in soup.select("th")[0].strings]
    data.append(lines)

output = open("boards.txt", "w")
for row in data:
    output.write("\t".join(row) + "\n")
output.close()
