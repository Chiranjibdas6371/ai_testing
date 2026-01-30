from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""

    if request.method == "POST":
        prompt = request.form["prompt"]
        response = model.generate_content(prompt)
        response_text = response.text

    return render_template("index.html", result=response_text)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

