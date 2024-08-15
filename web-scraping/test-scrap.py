# import requests
# from bs4 import BeautifulSoup

# get_url = 'http://127.0.0.1:3000/matrialize_demo.html'

# give_response = requests.get(get_url)
# print(give_response.status_code)
# #200

# soup = BeautifulSoup(give_response.content, 'html.parser')   #<--------------- small code example :>
# print(soup.prettify())


"""
Web scraping is the process of extracting data from websites. Python, with its rich ecosystem of libraries, is a popular choice for this task. The requests library is a fundamental tool for making HTTP requests to fetch web page content.

This script demonstrates how to scrape a web page using the requests and BeautifulSoup libraries.

Example:
    >>> scrape_web_page('http://127.0.0.1:3000/matrialize_demo.html')
    Request successful! 200
    <html>
      <head>
        ...
      </head>
      <body>
        ...
      </body>
    </html>
"""
import requests
from bs4 import BeautifulSoup

# URL to scrape
get_url = 'http://127.0.0.1:3000/matrialize_demo.html'

try:

    give_response = requests.get(get_url)

    if (give_response.status_code == 200):
        print(f"Request successful! {give_response.status_code}")

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(give_response.content, 'html.parser')

        # Print the prettified HTML
        print(soup.prettify())

    else:
        print("Failed to retrieve page")

except requests.exceptions.RequestException as e:
    print("An error occurred: ", e)
