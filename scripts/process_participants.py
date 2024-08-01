from csv import DictReader
import ast
import pandas as pd

match_list = []

with open("inputs/filtered_match_list.csv") as f:
    reader = DictReader(f)
    for lol_match in reader:
        for p in ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10",]:
            player = ast.literal_eval(lol_match[p])
            champ_name = player["championName"].lower()
            if champ_name == "monkeyking":
                champ_name = "wukong"
            position = player["teamPosition"].lower()
            lol_match[p] = champ_name + position
        team1 = ast.literal_eval(lol_match["team1"])
        lol_match["team1Win"] = team1["win"]
        lol_match.pop("team1")
        lol_match.pop("team2")
        lol_match.pop("")
        lol_match.pop("endOfGameResult")
        lol_match.pop("gameId")
        match_list.append(lol_match)

df = pd.DataFrame(match_list)
df.to_csv("outputs/key_filtered_match_list.csv")