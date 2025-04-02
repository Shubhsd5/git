from flask import Flask, render_template, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load API key from environment variable
api_key = os.getenv("groq_api")
client = Groq(api_key=api_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    
    
    user_input = request.get_json('question')

    prompt = f""" 
                
               {user_input}
                    
                """
    # Create prompt for Groq model
    response = client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {"role": "user", "content": prompt},
        ],
        model="llama-3.3-70b-versatile", 
    )
    
    
    answer = response.choices[0].message.content
    
    print("hello")
    return jsonify({'answer': answer})



if __name__ == '__main__':
    app.run(debug=True)
