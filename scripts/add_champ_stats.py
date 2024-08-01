from csv import DictReader
import ast
import json
import pandas as pd

match_list = []
with open("inputs/champ_stats.json") as f:
    champ_stats = json.load(f)

with open("inputs/key_filtered_match_list.csv") as f:
    reader = DictReader(f)
    for lol_match in reader:
        for p in ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10"]:
            champ = champ_stats.get(lol_match[p])
            if champ:
                win_rate = champ["win_rate"]
                pick_rate = champ["pick_rate"]
                ban_rate = champ["ban_rate"]
            else:
                win_rate = 0.0
                pick_rate = 0.0
                ban_rate = 0.0
            lol_match[p+"win_rate"] = win_rate
            lol_match[p+"pick_rate"] = pick_rate
            lol_match[p+"ban_rate"] = ban_rate
            lol_match.pop(p)
        lol_match.pop("")
        match_list.append(lol_match)

df = pd.DataFrame(match_list)
print(df)
df.to_csv("outputs/dataset.csv", index=False)