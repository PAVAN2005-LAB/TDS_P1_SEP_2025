# 🧠 LLM App Builder & Deployer

This project is a **FastAPI-based automation service** that can build, deploy, and update web applications automatically using **LLMs (Gemini / GPT)** and **GitHub Pages**.

It receives a brief from a remote API, uses a Large Language Model to generate code files, creates a GitHub repository, deploys it via GitHub Pages, and notifies an evaluation server when done.

---

## 🚀 Features
- **FastAPI endpoint** to receive task briefs (`/api-endpoint`)
- **Secret verification** for secure requests
- **LLM integration** (Gemini or GPT) to generate web app code from natural language
- **Automatic GitHub repo creation**
- **GitHub Pages deployment**
- **Evaluation callback** to the instructor’s server
- **Update support** for Round 2 (regenerates and redeploys)

---

## 🧩 Project Structure
.
├── main.py # FastAPI backend for the automation

├── requirements.txt # Python dependencies
ALSO INCLUDED DOCKER FILE ALSO 
├── README.md # Project documentation

├── .env # Environment variables (not committed)


## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<PAVAN>/TDS_P1_SEP_2025.git
cd TDS_P1_SEP_2025
### 2️⃣ Install Dependencies
pip install -r requirements.txt
###3️⃣ Create a .env File

Add the following keys:

GEMINI_API_KEY=your_gemini_api_key
GITHUB_TOKEN=your_github_pat
GITHUB_USERNAME=your_github_username
STUDENT_SECRET=your_secret_value
💡 Your STUDENT_SECRET should match the one you submitted in the Google Form.

###4️⃣ Run the API Server
uvicorn main:app --reload --port 8000


This runs your endpoint locally at:

http://127.0.0.1:8000/api-endpoint


You can expose it to the internet using ngrok
:

ngrok http 8000

###🧠 Example Request

Send a POST request to your API:

curl -X POST https://<your-ngrok-url>/api-endpoint \
  -H "Content-Type: application/json" \
  -d '{
    "email": "student@example.com",
    "task": "captcha-solver-123",
    "brief": "Create a simple web app that generates and validates CAPTCHAs.",
    "secret": "your_secret_value",
    "round": 1,
    "nonce": "xyz123",
    "evaluation_url": "https://tds.project-server.edu/eval"
  }'

###🧩 What Happens Internally

The request is received and validated.

The brief is sent to Gemini / GPT for app generation.

Files are saved and pushed to a new GitHub repository.

GitHub Pages is enabled for deployment.

A callback POST is sent to the evaluation URL with:

Repo URL

Commit SHA

Pages URL

###🔁 Round 2 (Update)

When a new POST arrives with the same task and "round": 2,
the system:

Pulls the previous repo

Generates updates via the LLM

Pushes changes

Re-deploys

Sends a second evaluation callback

🧾 Example Response (from your endpoint)
{
  "status": "accepted"
}

📡 Example Evaluation Callback Payload
{
  "email": "student@example.com",
  "task": "captcha-solver-123",
  "round": 1,
  "nonce": "xyz123",
  "repo_url": "https://github.com/YOUR_USERNAME/captcha-solver-123",
  "commit_sha": "d41d8cd9",
  "pages_url": "https://YOUR_USERNAME.github.io/captcha-solver-123/"
}

###🧰 Tech Stack

Python 3.10+

FastAPI

httpx

dotenv

OpenAI / Gemini API

GitHub REST API

AsyncIO

###🧑‍💻 Author

Pavan Kumar Yadav
3rd Year Engineering Student
Project: TDS_P1_SEP_2025


---

