from time import sleep
import requests

class RiotAPIClient():
    def __init__(self, endpoint, api_key) -> None:
        self.endpoint = endpoint
        self.header = {"X-Riot-Token": api_key}
    
    def request_api(self, url):
        while True:
            try:
                resp = requests.get(url, headers=self.header)
                if resp.status_code == 200:
                    return resp
                elif resp.status_code == 429:
                    sleep(5)
                else:
                    print(resp.status_code)
            except Exception as e:
                print(e)
    
    def get_grandmasters_by_queue(self, region, queue):
        print(f"Getting grandmasters in {region}-{queue}")
        resp = self.request_api(f"https://{region}.{self.endpoint}/lol/league/v4/grandmasterleagues/by-queue/{queue}")
        if resp:
            return resp.json()["entries"]
    
    def get_match_ids_by_puuid(self, region, puuid):
        print(f"Getting match ids by {region}-{puuid}")
        resp = self.request_api(f"https://{region}.{self.endpoint}/lol/match/v5/matches/by-puuid/{puuid}/ids?count=50")
        if resp:
            return resp.json()

    def get_summoner_by_summoner_id(self, region, summoner_id):
        print(f"Getting summoner by {region}-{summoner_id}")
        resp = self.request_api(f"https://{region}.{self.endpoint}/lol/summoner/v4/summoners/{summoner_id}")
        if resp:
            return resp.json()
    
    def get_match_by_match_id(self, region, match_id):
        print(f"Getting match in {region}-{match_id}")
        resp = self.request_api(f"https://{region}.{self.endpoint}/lol/match/v5/matches/{match_id}")
        if resp:
            return resp.json()