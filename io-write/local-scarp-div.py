"""
This script sends a GET request to a local URL, scrapes the HTML content, and extracts all div elements.

This will send a GET request to http://127.0.0.1:3000/matrialize_demo.html, scrape the HTML content, and extract all div elements, saving them to a file named "div.html".

In this code I used my made html webpage for test 
"""

import io
import requests
from bs4 import BeautifulSoup


def send_get_request(url):
    """
    Send a GET request to the specified URL and return the response.

    """
    return requests.get(url)


def scrape_html(response):
    """
    Scrape the HTML content of the response and extract all div elements.

    Args:
        response (requests.Response): The response object

    Reurns:
        list: A list of BeautifulSoup Tag objects representing the div elementst

    Example:
        >>> response = send_get_request('http://127.0.0.1:3000/matrialize_demo.html')
        >>> div_elements = scrape_html(response)
        >>> print(div_elements)
        [<div>...</div>, <div>...</div>, ...]
    """
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.find_all("div")
    else:
        return None
    
def save_div_elements_to_file(div_elements, filename):
    """
    Save the div elements to a file.

    Example:
        >>> div_elements = scrape_html(response)
        >>> save_div_elements_to_file(div_elements, 'div.html')
    """
    with io.open(filename, "w") as f:
        f.write(str(div_elements))


def main():
    """
    Main function to send the GET request, scrape the HTML content, and save the div elements to a file.

    """
    url = 'http://127.0.0.1:3000/matrialize_demo.html'
    response = send_get_request(url)
    div_elements = scrape_html(response)
    save_div_elements_to_file(div_elements, 'div.html')


if __name__ == "__main__":
    main()
