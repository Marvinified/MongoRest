from flask import request
from index import app
from bson.objectid import ObjectId
import json
from utils.database import db
from utils.serialise import serialise_document, response


@app.route("/query", methods=["POST"])
def delete():
    # Insert Document

    try:
        query = {"_id": ObjectId(request.json["id"])}
        document = db.data.find_one(query)
        document = serialise_document(document)

        return response(document, True)

    except Exception as error:
        print(error)
        return response(str(error), False)
