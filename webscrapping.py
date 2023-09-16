import requests
from bs4 import BeautifulSoup
import json

# URL of the website you want to scrape (replace with your chosen website)
url = 'https://example.com/products'

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define a list to store the scraped product data
    products = []

    # Find and extract product details (you can adapt this based on the website structure)
    product_elements = soup.find_all('div', class_='product')
    for product_element in product_elements:
        product_name = product_element.find('h2', class_='product-name').text.strip()
        product_price = product_element.find('span', class_='product-price').text.strip()
        product_description = product_element.find('p', class_='product-description').text.strip()

        # Create a dictionary to store the product information
        product_info = {
            'name': product_name,
            'price': product_price,
            'description': product_description
        }

        # Add the product information to the list
        products.append(product_info)

    # Store the scraped data in a JSON file
    with open('scraped_products.json', 'w', encoding='utf-8') as json_file:
        json.dump(products, json_file, ensure_ascii=False, indent=4)

    print(f'Successfully scraped {len(products)} products.')
else:
    print(f'Failed to retrieve the web page. Status code: {response.status_code}')
