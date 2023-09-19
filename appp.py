from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_cors import CORS

from flask_helmet import FlaskHelmet

import os, warnings, sys
warnings.simplefilter("ignore")
sys.setrecursionlimit(10**7)

app = Flask(__name__)
CORS(app)

helmet = FlaskHelmet()
helmet.init_app(app)

limiter = Limiter(app)

@app.route('/bfhl', methods=['GET', 'POST'])
@limiter.limit("60/minute")  # Adjust the rate limit as needed
def bfhl():
    if request.method == 'POST':
        user_id = request.json.get('user_id')

        if user_id.lower()!="shashwat_chouhan_16062001":
            return jsonify({"is_success": False}), 200
            
        response = {
            "is_success": True,
            "user_id": "shashwat_chouhan_16062001",
            "email" : "Shashwat.chouhan2020@vitbhopal.ac.in",
            "roll_number":"20BCE10676",
            "numbers": ["16","06","2001"],
            "alphabets": ['u', 'h', 's', 't', 'w', 'a', 'n', 'o', '_', 'c'],
            "highest_alphabet":["w"]
        }
        return jsonify(response), 200

    elif request.method == 'GET':
        response = {
            "operation_code":1
        }
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80, ssl_context="adhoc")
