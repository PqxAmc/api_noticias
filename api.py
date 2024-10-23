import requests
from flask import Flask, jsonify

app = Flask(__name__)

API_KEY = 'SUA_API_KEY_DO_NEWSAPI'  # Insira sua chave API do NewsAPI aqui
BASE_URL = 'https://newsapi.org/v2/top-headlines'

def get_top_news():
    params = {
        'apiKey': API_KEY,
        'language': 'en',  # ou 'pt' para português
        'category': 'general',
    }
    response = requests.get(BASE_URL, params=params)
    news_data = response.json()
    return news_data['articles'][:5]  # Retorna as 5 principais notícias

@app.route('/api/news', methods=['GET'])
def news():
    articles = get_top_news()
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
