# ASGURD.WORLD-PYTHON-TASK
Task 1: AWS EC2 Instance Management

Objective: I will be evaluating my proficiency in managing AWS EC2 instances using Python.

1. Importing the Necessary Libraries:
boto3: This library is used to interact with Amazon Web Services (AWS) resources, including EC2 instances.
datetime: This module is used for working with dates and times.
time: This module provides various time-related functions, including a function for introducing
2. Initializing the EC2 Client:
Here, we create an EC2 client object using Boto3. This client allows us to interact with EC2 instances and perform actions like starting and stopping them
    
    
3. Defining Instance Parameters:
In this section, you specify the parameters for launching an EC2 instance. These parameters include the Amazon Machine Image (AMI) ID, instance type, key pair name for SSH access, security group, subnet, and more. Make sure to replace the placeholders (e.g., 'your-ami-id') with your actual values.

4. Launching the EC2 Instance:
This code launches the EC2 instance using the parameters defined earlier. It then extracts the instance ID from the response and prints it to the console.
5. Defining Functions to Start and Stop the Instance:
These two functions, stop_instance and start_instance, use Boto3 to stop and start the EC2 instance, respectively. They take the instance_id as an argument and then call the appropriate EC2 API methods.

6. Configuring the Instance to Run on Specific Days and Times:
his is the main loop of the script. It runs indefinitely (you may want to implement a better exit strategy in a production environment). Inside the loop, it does the following:
Retrieves the current date and time using datetime.now().
Determines the current day of the week using now.weekday(), where 0 represents Monday, 1 represents Tuesday, and so on.
Checks if it's a Monday, Wednesday, Friday, or Sunday and if the current time is between 9:00 AM and 11:30 AM GMT.
If the conditions are met, it starts the EC2 instance using start_instance(). Otherwise, it stops the instance using stop_instance().
Sleeps for 60 seconds before checking again. This delay prevents the script from running too frequently and consuming unnecessary resources.
In summary, this script automates the management of an EC2 instance by starting it during specific days and times and stopping it during the remaining time to save costs. It continuously checks the current day and time and takes appropriate actions accordingly.

Task 2: Web Scraping

Objective: I will demonstrate web scraping proficiency using Python.

1. Importing the Necessary Libraries:
requests: This library is used to send HTTP requests to a website and retrieve its HTML content.
BeautifulSoup: This library allows you to parse HTML content and extract data from it.
json: This library is used to work with JSON data for storing the scraped information.

import requests
from bs4 import BeautifulSoup
import json

1. Specifying the Target URL:
In this line, you specify the URL of the website you want to scrape.
Replace 'https://example.com/products' with the actual URL of the website you want to scrape.

url = 'https://example.com/products'

2. Sending an HTTP GET Request:
This code sends an HTTP GET request to the specified URL to retrieve the web page's HTML content. It stores the response in the response variable.

response = requests.get(url)

3. Checking the HTTP Response:
Here, the script checks if the HTTP response status code is 200, which indicates a successful request. A status code of 200 means that the web page was successfully retrieved.

if response.status_code == 200:

4. Parsing the HTML Content:
Beautiful Soup is used to parse the HTML content of the web page. It converts the HTML into a structured tree-like format, making it easier to navigate and extract data.

soup = BeautifulSoup(response.text, 'html.parser')

5. Extracting Product Details:

This section of the code is responsible for scraping product details. It does the following:

Initializes an empty list called products to store the scraped data.
Uses Beautiful Soup to find all HTML elements with the class name 'product' (you should adapt this based on the website's structure).
For each product element found, it extracts the product's name, price, and description by searching for specific HTML elements and their associated class names.
Creates a dictionary product_info to store the extracted data for each product.
Appends product_info to the products list.

products = []

6. Find and extract product details (you can adapt this based on the website structure)

product_elements = soup.find_all('div', class_='product')
for product_element in product_elements:
product_name = product_element.find('h2', class_='product-name').text.strip()
product_price = product_element.find('span', class_='product-price').text.strip()
product_description = product_element.find('p', class_='product-description').text.strip()

```
# Create a dictionary to store the product information
product_info = {
    'name': product_name,
    'price': product_price,
    'description': product_description
}

# Add the product information to the list
products.append(product_info)

```

7. Storing the Scraped Data in a JSON File:

This code block opens a JSON file named 'scraped_products.json' in write mode and writes the scraped product data to it in a structured JSON format. The ensure_ascii=False parameter ensures that non-ASCII characters are properly encoded, and indent=4 formats the JSON data for readability.

with open('scraped_products.json', 'w', encoding='utf-8') as json_file:
json.dump(products, json_file, ensure_ascii=False, indent=4)

8. Outputting a Success Message:
Finally, the script prints a success message indicating the number of products successfully scraped.

You can adapt this script for your specific web scraping needs by customizing the HTML elements and class names used to extract data and by replacing the url variable with the URL of the website you want to scrape.

print(f'Successfully scraped {len(products)} products.')

