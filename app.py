#!/usr/bin/python3
from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
headers = {'User-Agent': 'cryptobuzz-app 1.0'}
news_data_key = os.getenv('NEWS_DATA_KEY')
news_api_key = os.getenv('NEWS_API_KEY')
PORT = os.getenv('PORT') or 5000

try:
    Airdrops = requests.get('https://api.airdropking.io/airdrops/?amount=10&order=best').json()
except Exception:
    Airdrops=[]
    
try:
    Reddit_posts = requests.get('https://www.reddit.com/r/cryptocurrency/hot.json?limit=9', allow_redirects=False, headers=headers).json()['data']['children']
except Exception:
    Reddit_posts = ["Couldn't Fetch"]
    
try:
    latest_news = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news,the-verge&apiKey={}'.format(news_api_key)).json().get('articles')
except Exception:
    latest_news = []

try:
    hot_news = requests.get('https://newsapi.org/v2/everything?q=cryptocurrency&apiKey={}'.format(news_api_key)).json().get('articles')
except Exception:
    hot_news = []

@app.errorhandler(404)
def not_found(e):
    render_template('404.html')

@app.route('/')
def home():
    return render_template('index.html', airdrops=Airdrops,
    reddit=Reddit_posts[2:8],
    latest_news=latest_news,
    hot_news=hot_news)

@app.route('/news')
def news_page():
    return render_template('news_gallery.html',
    hot_news=hot_news)
    
@app.route('/airdrops')
def airdrop_page():
    return render_template('airdrops.html', airdrops=Airdrops)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
