from modules.jikan import fetch_recommendation
from modules.utils import write_json


def test():
    write_json("api2.json", fetch_recommendation(50265))
    print("done!")


if __name__ == "__main__":
    test()
