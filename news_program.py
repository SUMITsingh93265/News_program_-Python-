# Use the Newsapi and the requests module to fetched the daily news related to different topic.

import requests
import pyttsx3

url = f'https://newsapi.org/v2/everything?q=indian-share-market&from=2024-06-14&to=2024-06-14&sortBy=popularity&apiKey=49de0445b14e4127a65e3fd6f4aec9fa'
news = requests.get(url).json()
article = news['articles']
news_articles = []
engine = pyttsx3.init()
engine.say("News are...")
for art in article:
    news_articles.append(art['title'])

for i in range(len(news_articles)):
    print(news_articles[i])
    engine.say(news_articles[i])

print()
print("Thanks for using.")
engine.say("Thanks for using.")
engine.runAndWait()