"""
This script sends a GET request to a specified URL, checks the status code, and performs HTML scraping using BeautifulSoup.

This will send a GET request to http://127.0.0.1:3000/matrialize_demo.html, print the status code, and save the HTML content to a file named "index.html".
"""

import io
import requests
from bs4 import BeautifulSoup


def send_get_request(url):
    """
    Send a GET request to the specified URL and return the response.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        requests.Response: The response object.
    """
    return requests.get(url)


def scrape_html(response):
    """
    Perform HTML scraping on the response content using BeautifulSoup.

    Args:
        response (requests.Response): The response object.

    Returns:
        str: The HTML content as a string.
    """
    if response.status_code == 200:
        print(f"Request successful! {response.status_code}")
        req = response.content
        soup = BeautifulSoup(req, 'html.parser')
        return str(soup)
    else:
        print(f"Error;-; {response.status_code} request failed")
        return None


def save_html_to_file(html_content, filename):
    """
    Save the HTML content to a file.

    Args:
        html_content (str): The HTML content as a string.
        filename (str): The filename to save the content to.
    """
    with io.open(filename, "w") as f:
        f.write(html_content)


def main():
    """
    Main function to send the GET request, scrape the HTML, and save it to a file.
    """
    url = 'http://127.0.0.1:3000/matrialize_demo.html'
    response = send_get_request(url)
    html_content = scrape_html(response)
    if html_content:
        save_html_to_file(html_content, "index.html")


if __name__ == "__main__":
    main()
