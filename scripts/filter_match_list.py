import pandas as pd
import ast

match_list = pd.read_csv("inputs/match_list.csv", converters={"teams": lambda x: ast.literal_eval(x),
                                                                     "participants": lambda x: ast.literal_eval(x)})
classic_match_list = match_list[match_list["gameMode"] == "CLASSIC"]
version_match_list = classic_match_list[classic_match_list["gameVersion"].str.startswith("14.10")]
complete_match_list = version_match_list[version_match_list["endOfGameResult"] == "GameComplete"]
complete_match_list[["team1","team2"]] = pd.DataFrame(complete_match_list.teams.tolist(), index= complete_match_list.index)
complete_match_list[["p1","p2","p3","p4","p5",
                     "p6","p7","p8","p9","p10"]] = pd.DataFrame(complete_match_list.participants.tolist(), 
                                                                index= complete_match_list.index)
column_match_list = complete_match_list.filter(["endOfGameResult",
                                               "gameId",
                                               "p1",
                                               "p2",
                                               "p3",
                                               "p4",
                                               "p5",
                                               "p6",
                                               "p7",
                                               "p8",
                                               "p9",
                                               "p10",
                                               "team1",
                                               "team2"])

column_match_list.to_csv("/home/cubone/LOLMatchPredictor/outputs/filtered_match_list.csv")