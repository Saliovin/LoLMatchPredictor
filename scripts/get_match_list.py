from concurrent.futures import ThreadPoolExecutor
import os
import pandas as pd
from dotenv import load_dotenv
from RiotAPIClient import RiotAPIClient

load_dotenv(override=True)

client = RiotAPIClient(os.getenv("API_ENDPOINT"), os.getenv("API_KEY"))
players = client.get_grandmasters_by_queue("ph2", "RANKED_SOLO_5x5")
match_list = {}

def retrieve_match(match_id):
    if match_list.get(match_id):
        return None
    else:
        return client.get_match_by_match_id("sea", match_id)

for player in players:
    summoner = client.get_summoner_by_summoner_id("ph2", player["summonerId"])
    match_ids = client.get_match_ids_by_puuid("sea", summoner["puuid"])

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(retrieve_match, match_id) for match_id in match_ids]
        for future in futures:
            result = future.result()
            if result:
                match_list[result["metadata"]["matchId"]] = result["info"]

pd_match_list = pd.DataFrame(list(match_list.values()))
pd_match_list.to_csv("/home/cubone/LOLMatchPredictor/outputs/match_list.csv")