from flask import Flask, request
import os

from pymongo import MongoClient
from pymongo.server_api import ServerApi

from tools import calculate_premium, convert_bson_to_python

app = Flask(__name__)
uri = os.environ["DATABASE_URI"]
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["test"]


@app.route('/rates', methods=['POST'])
def get_rates():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json_request = request.json
    else:
        return 'Content-Type not supported!'

    try:
        query = {
            "SumInsured": json_request["SumInsured"],
            "TierID": json_request["TierID"],
            "Tenure": json_request["Tenure"],
            "Age": {"$in": json_request["Ages"]}
        }
    except Exception as e:
        return "Error parsing request data"

    try:
        db_response = db.rates.find(query)
        db_response_clean = convert_bson_to_python(db_response)
        calculated_premiums = calculate_premium(db_response_clean)
        return calculated_premiums

    except Exception as e:
        print(e)
        return f"Some error connecting to Database \n {str(e)}"
