from flask import Flask
import os

from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
uri = os.environ["DATABASE_URI"]
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["test"]


@app.route('/rates')
def get_rates():
    dummy_request_params = {
        "SumInsured": "5000",
        "TierID": "1",
        "Tenure": "1",
        "Ages": ["46", "35", "10"]
    }

    query = {
        "SumInsured": 500000,
        "TierID": 1,
        "Tenure": 1,
        "Age": {"$in": [46, 35, 10]}
    }

    try:
        db_response = db.rates.find(query)
        ans = list()

        for resp in db_response:
            row = dict()
            for k, v in resp.items():
                if k != "_id":
                    row[k] = v
            ans.append(row)

        print(ans)
        return ans

    except Exception as e:
        print(e)
        return f"Some error connecting to Database \n {str(e)}"
