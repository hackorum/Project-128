from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL)
soup = BeautifulSoup(page.text, "html.parser")
tables = soup.find_all("table")
l = []
table_rows = tables[4].find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    l.append(row)


names = []
distance = []
mass = []
radius = []


for i in range(1, len(l)):
    names.append(l[i][0])
    distance.append(l[i][5])
    mass.append(l[i][7])
    radius.append(l[i][8])

df = pd.DataFrame(
    list(
        zip(
            names,
            distance,
            mass,
            radius,
        )
    ),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)
df.to_csv("data.csv")
