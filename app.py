from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

SECRET = os.getenv("SECRET")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "TDS student API running!"})

@app.route("/api", methods=["POST"])
def handle_task():
    data = request.get_json(force=True)

    # Verify secret
    if data.get("secret") != SECRET:
        return jsonify({"error": "Invalid secret"}), 403

    # Extract info from request
    email = data.get("email")
    task = data.get("task")
    round_ = data.get("round")
    nonce = data.get("nonce")
    brief = data.get("brief")
    evaluation_url = data.get("evaluation_url")

    # Respond immediately with 200 OK
    response = {"status": "ok", "message": "Task received"}
    
    # Simulate background task: (in real case, build app & push to GitHub)
    print(f"Received task: {task}")
    print(f"Brief: {brief}")

    # After building/deploying, send a POST to evaluation_url
    payload = {
        "email": email,
        "task": task,
        "round": round_,
        "nonce": nonce,
        "repo_url": "https://github.com/yourusername/sample-repo",
        "commit_sha": "abc123",
        "pages_url": "https://yourusername.github.io/sample-repo/"
    }

    try:
        r = requests.post(evaluation_url, json=payload, headers={"Content-Type": "application/json"})
        print("Posted to evaluation URL:", r.status_code)
    except Exception as e:
        print("Error posting to evaluation URL:", e)

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
