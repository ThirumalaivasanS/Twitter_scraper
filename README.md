
# Twitter Scraper

This is a simple Python script that allows you to scrape tweets based on a specified keyword or hashtag, start and end dates, and number of tweets. The scraped data is then stored in a MongoDB database and can be downloaded as CSV or JSON files.


## Prerequisites
Before running this script, you will need to have the following installed:
1. Python 3.x
2. MongoDB
3. Required Python libraries (pandas, snscrape, pymongo, and datetime)

## Getting started
1. Clone this repository to your local machine.
2. Install the required Python libraries by running pip install -r requirements.txt.
3. Make sure MongoDB is running on your local machine. And make sure you have a MongoDB instance running and update the client variable in the script with the appropriate connection string.
4. Start the Streamlit app by running streamlit run twitter_scraper.py in your terminal.
5. Enter the desired keyword or hashtag, start and end dates, and number of tweets in the input fields and click the "Search" button.
6. The scraped data will be displayed in a table and can be downloaded as CSV or JSON files using the provided links.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

Contributions are always welcome!



## Credits
This script was created by Thirumalaivasan S.Feel free to modify and use it for your own purposes. If you have any questions or suggestions, please contact me at thirumalaivasan.subramanian@gmail.com