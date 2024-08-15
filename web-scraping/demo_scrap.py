import requests
from bs4 import BeautifulSoup

get_url = 'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

get_request = requests.get(get_url)
print(f"Here is the status code: {get_request.status_code}")


# product_details = {}
# product_price = {}
# product_reviews = {}

def details():
    if get_request.status_code == 200:
        print(f"Request successful! {get_request.status_code}")
        req = get_request.content
        soup = BeautifulSoup(req, 'html.parser')
        divs = soup.find_all(class_='KzDlHZ')
        return [div.text for div in divs]
    else:
        print(f"Error: {get_request.status_code}")
        return None


def scap_prices():
    if get_request.status_code == 200:
        print(f"Request successful! {get_request.status_code}")
        req = get_request.content
        soup = BeautifulSoup(req, 'html.parser')
        prices = soup.find_all(class_='Nx9bqj _4b5DiR')
        return [price.text for price in prices]

    else:
        print(f"Error: {get_request.status_code}")
        return None


def scrap_reviews():
    if get_request.status_code == 200:
        print(f"Request succesful! {get_request.status_code}")
        req = get_request.content
        soup = BeautifulSoup(req, 'html.parser')
        reviews = soup.find_all(class_='XQDdHH')
        return [review.text for review in reviews]
    else:
        print(f"Error;-; {get_request.status_code}")
        return None


# ========================================================================================
# this main function call upper functions and print deatils of products in simple output
# =======================================================================================

def main():

    divs = details()
    if divs is not None:
        for div in divs:
            print(div)

    else:
        print("No deatils found or error in request.")

    prices = scap_prices()
    if prices is not None:
        for price in prices:
            print(price)
        

    else:
        print("NO prces found or error in request ")

    reviews = scrap_reviews()
    if reviews is not None:
        for review in reviews:
            print(review)
           
    else:
        print(f"NO reveiws found or error in request")

   


if __name__ == "__main__":
    main()


# ===============================================================================================
# this main function call upper functions and print deatils of products in dictionary format
# ================================================================================================

# def main():
#     divs = details()
#     prices = scap_prices()
#     reviews = scrap_reviews()

#     if divs is not None and prices is not None and reviews is not None:
#         for i in range(len(divs)):
#             product = divs[i]
#             product_details[product] = {}
#             product_details[product]['price'] = prices[i]
#             product_details[product]['review'] = reviews[i]
#     else:
#         print("No details found or error in request.")

#     print("Product Details:", product_details)


# if __name__ == "__main__":
#     main()
