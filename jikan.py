import requests
from utils import write_json


class Jikan:
    def fetch_recommendation(malid):
        malid_dict = {}
        api_dict = {}
        api_list = []

        def _fr_map_recommendation_malids():
            api_recommendations = f"https://api.jikan.moe/v4/anime/{malid}/recommendations"
            temp = requests.get(api_recommendations)
            res = temp.json()

            for i, key in enumerate(res["data"]):
                malid_dict[i] = key["entry"]["mal_id"]

        def _fr_map_recommendation_apis():
            for i in malid_dict:
                api_dict[i] = f"https://api.jikan.moe/v4/anime/{malid_dict[i]}/"

        def _fr_fetch_apis():
            for i in api_dict:
                temp = requests.get(api_dict[i])
                res = temp.json()
                api_list.append(res)

        RESULTS_API = {"results": api_list}

        _fr_map_recommendation_malids()
        _fr_map_recommendation_apis()
        _fr_fetch_apis()

        write_json("api.json", RESULTS_API)
        print("done!")
