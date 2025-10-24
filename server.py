from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/check_title/<title_id>", methods=["GET"])
def check_title(title_id):
    url = f"https://{title_id}.playfabapi.com"
    try:
        resp = requests.head(url, timeout=5)  # simple HEAD request
        return jsonify(valid=True)
    except requests.RequestException:
        return jsonify(valid=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
