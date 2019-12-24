from flask import request
from index import app

@app.route('/insert', methods=['POST'])
def insert():
    return "Insert route!" 