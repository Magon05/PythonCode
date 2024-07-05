import requests
from bs4 import BeautifulSoup

url = 'https://www.wildberries.ru/catalog/elektronika/tehnika-dlya-doma/telefony-statsionarnye'  # URL of the website
headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
    }
response = requests.get(url, headers)  # Send a GET request to the URL
soup = BeautifulSoup(response.text, 'lxml')  # Parse the HTML content

# Find and extract the elements containing product information and cashback
product_elements = soup.find_all('div', class_='product')
cashback_elements = soup.find_all('span', class_='bonus-percent')
#print(cashback_elements)
with open("log.txt", "w") as file:
    file.write(response.text)


# Process the extracted data to identify products with the highest cashback
# Example:
# highest_cashback_products = {}
# for product, cashback in zip(product_elements, cashback_elements):
#     product_name = product.find('h3').text
#     cashback_value = float(cashback.text.replace('% cashback', ''))
#     highest_cashback_products[product_name] = cashback_value

# Sort and display the products with the highest cashback
# Example:
# sorted_products = sorted(highest_cashback_products.items(), key=lambda x: x[1], reverse=True)
# for product, cashback in sorted_products:
#     print(f"{product}: {cashback}% cashback")