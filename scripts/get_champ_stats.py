from bs4 import BeautifulSoup
import requests
from string import ascii_letters
import pandas as pd

allowed = set(ascii_letters)
page = requests.get("https://www.op.gg/champions")
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find("table")
table_body = table.find("tbody")

stats_dict = {}
for row in table_body.find_all("tr"):
    data = row.find_all("td")
    if len(data) != 8:
        continue
    champ = ''.join(l for l in data[1].find("img")["alt"].lower() if l in allowed)
    position = ''.join(l for l in data[3].find("img")["alt"].lower() if l in allowed)
    if position == "support":
        position = "utility"
    win_rate = data[4].contents[0]
    pick_rate = data[5].contents[0]
    ban_rate = data[6].contents[0]

    stats_dict[champ+position] = {
        "win_rate": float(win_rate),
        "pick_rate": float(pick_rate),
        "ban_rate": float(ban_rate)
    }

df = pd.DataFrame(stats_dict)
df.to_json("outputs/champ_stats.json")