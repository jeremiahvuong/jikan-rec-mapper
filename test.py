from modules.jikan import fetch_recommendation
from modules.utils import write_json

FILE_NAME = "api"


def test():
    write_json(f"{FILE_NAME}.json", fetch_recommendation(50265))
    print("done!")


if __name__ == "__main__":
    test()
