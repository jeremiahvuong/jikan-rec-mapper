import requests
from utils import write_json


def fetch_recommendation(malid):
    malid_dict = {}
    api_dict = {}
    api_list = []

    api_recommendations = f"https://api.jikan.moe/v4/anime/{malid}/recommendations"
    temp = requests.get(api_recommendations)
    res = temp.json()

    for i, key in enumerate(res["data"]):
        malid_dict[i] = key["entry"]["mal_id"]

    for i in malid_dict:
        api_dict[i] = f"https://api.jikan.moe/v4/anime/{malid_dict[i]}/"

    for i in api_dict:
        temp = requests.get(api_dict[i])
        res = temp.json()
        api_list.append(res)

    RESULTS_API = {"results": api_list}

    write_json("api.json", RESULTS_API)
    print("done!")
