import requests
from bs4 import BeautifulSoup
import io
import time

get_url = 'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def fetch_content(url, headers, retries=5):
    """
    Fetches the content of a URL with retries.
    """
    for i in range(retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        elif response.status_code == 429:
            print(f"Rate limit exceeded. Retrying in {2 ** i} seconds...")
            time.sleep(2 ** i)
        else:
            print(f"Error: {response.status_code}")
            return None
    return None


def details(soup):
    """
    Extracts product details from the BeautifulSoup object.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object.

    Returns:
        list: A list of product details.
    """
    divs = soup.find_all(class_='KzDlHZ')
    return [div.text for div in divs]


def scrap_prices(soup):
    """
    Extracts prices from the BeautifulSoup object.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object.

    Returns:
        list: A list of prices.
    """
    prices = soup.find_all(class_='Nx9bqj _4b5DiR')
    return [price.text for price in prices]


def scrap_reviews(soup):
    """
    Extracts reviews from the BeautifulSoup object.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object.

    Returns:
        list: A list of reviews.
    """
    reviews = soup.find_all(class_='XQDdHH')
    return [review.text for review in reviews]


def main():
    """
    The main function that fetches the content, extracts details, prices, and reviews, and writes them to a file.
    """
    content = fetch_content(get_url, headers)
    if content:
        soup = BeautifulSoup(content, 'html.parser')

        divs = details(soup)
        prices = scrap_prices(soup)
        reviews = scrap_reviews(soup)

        with io.open("product-details.txt", "a", encoding="utf-8") as file:
            if divs:
                file.write("Product Details:\n")
                for div in divs:
                    file.write(div + "\n")
                print("Product details written to file.")

            if prices:
                file.write("\nPrices:\n")
                for price in prices:
                    file.write(price + "\n")
                print("Prices written to file.")

            if reviews:
                file.write("\nReviews:\n")
                for review in reviews:
                    file.write(review + "\n")
                print("Reviews written to file.")
    else:
        print("No details, prices, or reviews found or error in request.")


if __name__ == "__main__":
    main()

# This will fetch the content of the URL, extract product details, prices, and reviews, and write them to a file named "product-details.txt".
