from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/check_title/<title_id>", methods=["GET"])
def check_title(title_id):
    """
    Check if a PlayFab Title ID exists by hitting the Admin/GetTitleData endpoint.
    """
    url = f"https://{title_id}.playfabapi.com/Admin/GetTitleData"
    headers = {
        "Content-Type": "application/json",
        "X-SecretKey": "dummy"  # Dummy key; server responds even if invalid
    }
    try:
        resp = requests.post(url, json={}, headers=headers, timeout=5)
        # 200, 400, or 403 means Title exists
        if resp.status_code in [200, 400, 403]:
            return jsonify(valid=True)
        return jsonify(valid=False)
    except requests.RequestException:
        return jsonify(valid=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
