# React and Flask are on different ports so we need to allow 
# cross-origin requests.
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__) # creates web app and ask flask to take care of routing, request and responses
CORS(app)  # Allow React to talk to Flask


@app.route('/connect', methods=['POST']) #registers a route
def connect_vpn():
    print("VPN Connect request received")
    return jsonify({'status': 'Connected'})

if __name__ == '__main__':
    app.run(debug=True)