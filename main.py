from jikan import Jikan


# Example
MAL_ID = 50265


def main():
    Jikan.fetch_recommendation(MAL_ID)


if __name__ == "__main__":
    main()
