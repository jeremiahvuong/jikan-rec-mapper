from utils import write_json
import requests


def fetch_recommendation(malid: int) -> dict[str, list[object]]:
    malid_dict: dict[int, int] = {}
    api_list: list[object] = []

    API_REC_MALID = f"https://api.jikan.moe/v4/anime/{malid}/recommendations"
    temp = requests.get(API_REC_MALID)
    res = temp.json()

    for i, key in enumerate(res["data"]):
        malid_dict[i] = key["entry"]["mal_id"]

    for i in malid_dict:
        temp = requests.get(f"https://api.jikan.moe/v4/anime/{malid_dict[i]}/")
        res = temp.json()
        api_list.append(res)

    return {"results": api_list}


# Run to test module. To run api run main.py
if __name__ == "__main__":
    FILE_NAME = "api"
    MAL_ID = 50265

    write_json(f"{FILE_NAME}.json", fetch_recommendation(MAL_ID))
    print("done!")
