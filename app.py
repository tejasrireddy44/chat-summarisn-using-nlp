import google.generativeai as genai
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Initialize Flask App
app = Flask(__name__)
CORS(app) 

# Set up Google Gemini API Key 
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)

MODEL_NAME = "gemini-1.5-pro"


def summarize_chat(chat_text):
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        prompt = f"Summarize this conversation briefly:\n\n{chat_text}\n\nSummary:"
        response = model.generate_content(prompt)
        
       
        if hasattr(response, "text"):
            return response.text.strip()
        elif hasattr(response, "candidates"):
            return response.candidates[0].content.strip()
        else:
            return "Error: Unexpected API response format."

    except Exception as e:
        return f"Error: {str(e)}"

# Homepage route
@app.route('/')
def home():
    return render_template("index.html")

# API route for summarization
@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        chat_text = data.get("chat_text", "").strip()

        if not chat_text:
            return jsonify({"error": "No chat text provided"}), 400

        summary = summarize_chat(chat_text)
        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
