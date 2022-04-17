import requests
import json


class Jikan:
    def fetch_recommendation(malid):
        malid_dict = {}
        api_dict = {}
        api_list = []

        def _map_recommendation_malids():
            api_recommendations = f"https://api.jikan.moe/v4/anime/{malid}/recommendations"
            temp = requests.get(api_recommendations)
            res = temp.json()

            for i, key in enumerate(res["data"]):
                malid_dict[i] = key["entry"]["mal_id"]

        def _map_recommendation_apis():
            for i in malid_dict:
                api_dict[i] = f"https://api.jikan.moe/v4/anime/{malid_dict[i]}/"

        def _fetch_apis():
            for i in api_dict:
                temp = requests.get(api_dict[i])
                res = temp.json()
                api_list.append(res)

        def _write_json():
            with open("api.json", "w", encoding="utf-8") as f:
                results_api = {"results": api_list}
                json.dump(results_api, f, ensure_ascii=False, indent=2)

            print("done!")

        _map_recommendation_malids()
        _map_recommendation_apis()
        _fetch_apis()
        _write_json()
