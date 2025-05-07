from flask import Flask, request, jsonify, send_from_directory, render_template  
from flask_cors import CORS  
import google.generativeai as genai  
import os
import sqlite3
import re

app = Flask(__name__, static_folder='')  
CORS(app)  

GOOGLE_GEMINI_API_KEY = "AIzaSyCMcAh6-zCqit1HsXTfEoE2EgFUaEJJ7-U"
genai.configure(api_key=GOOGLE_GEMINI_API_KEY) 
chat_model = genai.GenerativeModel("gemini-1.5-flash")

def extract_keywords(text):
    stopwords = {'o', 'a', 'e', 'é', 'de', 'do', 'da', 'em', 'um', 'uma', 'para', 'com', 'que', 'se', 'não', 'por', 'os', 'as', 'no', 'na'}
    words = re.findall(r'\b\w+\b', text.lower())
    keywords = [word for word in words if word not in stopwords]
    return keywords

def query_rules(keywords):
    conn = sqlite3.connect('rpg_rules.db')
    c = conn.cursor()
    matched_rules = []
    for kw in keywords:
        c.execute("SELECT description FROM rules WHERE keywords LIKE ?", ('%'+kw+'%',))
        rows = c.fetchall()
        for row in rows:
            if row[0] not in matched_rules:
                matched_rules.append(row[0])
    conn.close()
    return matched_rules

def build_prompt(rules, user_message):
    prompt = "Você é um assistente que conhece as regras do RPG PvP. Responda de forma breve e objetivo. Baseado nas regras abaixo, responda à pergunta do jogador.\n\n"
    prompt += "Regras relevantes:\n"
    for rule in rules:
        prompt += "- " + rule + "\n"
    prompt += "\nPergunta do jogador: " + user_message + "\nResposta:"
    return prompt

@app.route('/chat', methods=['POST']) 
def chat_with_bot(): 
    try:
        data = request.json  
        user_message = data.get("message", "") 
        if not user_message: 
            return jsonify({"error": "mensagem vazia"}), 400  
        
        keywords = extract_keywords(user_message)
        rules = query_rules(keywords)
        prompt = build_prompt(rules, user_message)
        
        chat = chat_model.start_chat(history=[])
        response = chat.send_message(prompt)
        return jsonify({"reply": response.text}) 
    except Exception as e:
        print("Erro ao processar a requisição:", e)
        return jsonify({"error": "Erro interno no servidor. Tente novamente mais tarde."}), 500

@app.route('/')
def index():
    return send_from_directory('view', 'index.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True)  
