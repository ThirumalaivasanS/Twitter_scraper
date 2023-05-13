#Import the required libraries:
import snscrape.modules.twitter as sntwitter
import pandas as pd
from pymongo import MongoClient
from datetime import datetime

#Define the function to scrape tweets based on the specified criteria:
def scrape_tweets(keyword, start_date, end_date, num_tweets):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} since:{start_date} until:{end_date}').get_items()):
        if i >= num_tweets:
            break
        tweets.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.sourceUrl, tweet.likeCount])
    return pd.DataFrame(tweets, columns=['date', 'id', 'url', 'content', 'user', 'reply_count', 'retweet_count', 'language', 'source', 'like_count'])

#Create a dictionary to store the search criteria:
search_criteria = {
    'keyword': '',
    'start_date': '',
    'end_date': '',
    'num_tweets': 0,
    'scraped_date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
}

#Connect to the MongoDB database and create a collection:
client = MongoClient('mongodb://localhost:27017/')
db = client['twitter_db']
collection = db['tweets']

#Insert the scraped data and search criteria into the collection:
def insert_into_db(data, search_criteria):
    search_criteria['num_tweets'] = len(data)
    collection.insert_one({'search_criteria': search_criteria, 'data': data.to_dict('records')})

#Define the download functions for CSV and JSON files:
import base64

def download_csv(data):
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    return b64

def download_json(data):
    json_data = data.to_json(orient='records')
    b64 = base64.b64encode(json_data.encode()).decode()
    return b64

#Create a streamlit app to display the input fields and table:
import streamlit as st
st.title('Twitter Scraper')

# Input fields
keyword = st.text_input('Keyword or Hashtag')
start_date = st.date_input('Start Date')
end_date = st.date_input('End Date')
num_tweets = st.number_input('Number of Tweets', min_value=1, max_value=1000)

if st.button('Search'):
    # Scrape tweets
    data = scrape_tweets(keyword, start_date, end_date, num_tweets)
    
    # Insert into database
    search_criteria['keyword'] = keyword
    search_criteria['start_date'] = start_date.strftime('%d-%m-%Y')
    search_criteria['end_date'] = end_date.strftime('%d-%m-%Y')
    search_criteria['num_tweets'] = num_tweets
    insert_into_db(data, search_criteria)
    
    # Display table
    st.dataframe(data)
    
    # Download buttons
    st.markdown('### Download Data')
    st.markdown('<a href="data:file/csv;base64,{csv}">Download CSV File</a>'.format(csv=download_csv(data)), unsafe_allow_html=True)
    st.markdown('<a href="data:file/json;base64,{json}">Download JSON File</a>'.format(json=download_json(data)), unsafe_allow_html=True)




