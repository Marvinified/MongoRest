from flask import Flask, request

# Initialise app
app = Flask(__name__)

# Insert route
import routes.insert


# Default Route
@app.route("/", methods=["POST", "GET"])
def index():
    return {
        "message": "Welcome to Mongo REST", 
        "endpoints": {
            "/insert": {
                "description": "Insert data into the database"
            }
        }
    }

