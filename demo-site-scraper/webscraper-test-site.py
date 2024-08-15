import requests
from bs4 import BeautifulSoup

get_url = 'https://webscraper.io/test-sites/tables'


get_request = requests.get(get_url)
print(f"Request status is: {get_request.status_code}")

if get_request.status_code == 200:
    print(f"Request successful! {get_request.status_code}")
    req = get_request.content
    soup = BeautifulSoup(req, 'html.parser')

    scraping = soup.find_all(class_='tables-semantically-correct')
    with open("job-website-scrap-demo/text.txt", "w") as f:
        for scrap in scraping:
            print(scrap.text)
            f.write(scrap.text)
            f.write("\n\n")

    # if scarping:
    #     for scrap in scarping:
    #         first_name = scrap.find('a', class_='title fw500 ellipsis')
    #         last_name = scrap.find('a', class_=' comp-dtls-wrap')

    #         if first_name and last_name and location and experience:
    #             print(f"Job Title: {first_name.text.strip()}")
    #             print(f"Company: {last_name.text.strip()}")
    #             print('-' * 40)
    # else:
    #     print("No found.")
else:
    print(f"Error: {get_request.status_code}")
