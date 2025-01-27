#!/usr/bin/python3
"""
Apis for cryptobuzz webapp
author: Mirey-dev
"""
from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
headers = {'User-Agent': 'cryptobuzz-app 1.0'}
news_data_key = os.getenv('NEWS_DATA_KEY')
news_api_key = os.getenv('NEWS_API_KEY')
cg_api_key = os.getenv('CG_KEY')
PORT = os.getenv('PORT') or 5000

# Request Data to populate app
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
    
# try:
#     headers = {
# 		"accept": "application/json",
# 		"x-cg-demo-api-key": cg_api_key
# 	}
#     Cryptolist_trending = requests.get('https://api.coingecko.com/api/v3/search/trending', headers=headers).json()
#     coins = Cryptolist_trending.get('coins')
#     nfts = Cryptolist_trending.get('nfts')
#     categories = Cryptolist_trending.get('categories')
# except Exception:
#     Cryptolist_trending = []

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.route('/')
def home():
    """
    Define route for homepage
    """
    return render_template('index.html', airdrops=Airdrops,
    reddit=Reddit_posts[2:8],
    latest_news=latest_news,
    hot_news=hot_news,
    # coins=coins if len(coins) > 0 else [],
    # nfts=nfts if len(nfts) > 0 else [],
    # categories=categories if len(categories) > 0 else []
    )

@app.route('/news')
def news_page():
    """
    Define route for newspage
    """
    return render_template('news_gallery.html',
    hot_news=hot_news)
    
@app.route('/airdrops')
def airdrops_display():
    """
    Define route for airdrop page
    """
    return render_template('airdrops.html', airdrops=Airdrops)

@app.route('/about')
def about_us():
    """
    Define route for Landing page
    """
    return redirect('https://amahe8664.wixsite.com/cryptobuzz')

if __name__ == '__main__':
    app.run(port=PORT, debug=True)
