from flask import Flask
from flask import request, jsonify
from datetime import datetime, time, timedelta


app = Flask(__name__)

today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

# This is a hard-coded dictionary of competitions.
competitions = {"ADJCKDSJC": {"bids": [], "date": yesterday},
                "LAPLCKDSJL": {"bids": [], "date": tomorrow}}


@app.route("/")
def index():
    return {'hello': 'world'}

# Given a list of bids, returns minimum bid


def get_min_bid(bids):
    return min(bids)

# Endpoint to show winner given a competition id and a bid number


@app.route("/bids/<id>/<int:bid>")
def bid_status(id, bid):
    competitions.get(id)["bids"].append(bid)
    return jsonify('winner so far' if get_min_bid(competitions.get(id)["bids"]) == bid else 'loser')

# Endpoint to show winner so far given a competition unique id and a bid number
# If the competition exxpiry date is set for a time earlier than _now_, this will
# show "time expired"


@app.route("/bids_date/<id>/<int:bid>")
def bid_status_date(id, bid):
    currentTime = datetime.now()

    competitions.get(id)["bids"].append(bid)
    if currentTime > competitions.get(id)["date"]:
        return jsonify("Submission too late. The competition expiry date has passed.")
    elif get_min_bid(competitions.get(id)["bids"]) == bid:
        return 'winner so far'
    return 'loser'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
