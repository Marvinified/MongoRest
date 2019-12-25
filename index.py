from flask import Flask, request
import json

# Initialise app
app = Flask(__name__)

# Insert route
import routes.insert
import routes.query


# Load JSON Docs
with open("docs.json", "r") as docs:
    docs = json.load(docs)

# Default Route
@app.route("/", methods=["POST", "GET"])
def index():
    return docs

