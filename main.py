from flask import *
from modules.jikan import fetch_recommendation

app = Flask(__name__)


@app.route("/")
def home():
    return json.dumps({"types": ["recommendation"]})


@app.route('/recommendation/<int:MAL_ID>')
def recommendation(MAL_ID: int):
    return json.dumps(fetch_recommendation(MAL_ID), sort_keys=False)


if __name__ == "__main__":
    app.run(port=5000)
