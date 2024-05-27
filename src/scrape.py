import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_grocery_website(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        product_names = [item.get_text() for item in soup.select('.product-name')]
        prices = [item.get_text() for item in soup.select('.product-price')]
        availability = [item.get_text() for item in soup.select('.product-availability')]

        data = {'Product Name': product_names, 'Price': prices, 'Availability': availability}
        df = pd.DataFrame(data)
        
        return df
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

url = 'https://www.loblaws.ca/food/fruits-vegetables/c/28000?navid=flyout-L2-fruits-vegetables'
grocery_df = scrape_grocery_website(url)

if grocery_df is not None:
    print(grocery_df)
    grocery_df.to_csv('grocery_products.csv', index=False)
