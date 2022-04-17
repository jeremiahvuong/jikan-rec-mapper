import requests


def fetch_recommendation(malid) -> dict[str, list]:
    malid_dict = {}
    api_list = []

    API_REC_MALID = f"https://api.jikan.moe/v4/anime/{malid}/recommendations"
    temp = requests.get(API_REC_MALID)
    res = temp.json()

    for i, key in enumerate(res["data"]):
        malid_dict[i] = key["entry"]["mal_id"]

    for i in malid_dict:
        temp = requests.get(f"https://api.jikan.moe/v4/anime/{malid_dict[i]}/")
        res = temp.json()
        api_list.append(res)

    RESULTS_API = {"results": api_list}

    return RESULTS_API
