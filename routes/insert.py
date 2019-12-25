from flask import request
from index import app
import json
from utils.database import db
from utils.serialise import serialise_document, response


@app.route("/insert", methods=["POST"])
def insert():
    # Insert Document

    try:
        document = db.data.insert_one(request.json)

        if document.acknowledged:
            data = serialise_document(request.json)
            return response(data, True)
        else:
            return response("Can't insert document", False)

    except Exception as error:
        print(error)
        return response(str(error), False)
