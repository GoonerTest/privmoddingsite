from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # allow cross-origin requests from your HTML

@app.route("/check_title/<title_id>", methods=["GET"])
def check_title(title_id):
    """Check if the PlayFab API URL exists for the given Title ID"""
    url = f"https://{title_id}.playfabapi.com"
    try:
        resp = requests.get(url, timeout=3)
        if resp.ok or (300 <= resp.status_code < 400):
            return jsonify(valid=True)
        return jsonify(valid=False)
    except requests.RequestException:
        return jsonify(valid=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)