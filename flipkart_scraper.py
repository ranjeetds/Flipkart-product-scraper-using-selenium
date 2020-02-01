# Importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Intializing driver
driver = webdriver.Chrome("C:\\chromedriver\chromedriver.exe")

# Initializing required lists to store fetched data
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
Images=[]

# URL to fetch from Can be looped over / crawled multiple urls
driver.get('https://www.flipkart.com/laptops/laptops~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq=')

content = driver.page_source
soup = BeautifulSoup(content)

# Parsing content
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34'})
    image=a.find('div', attrs={'class':'_3n6o0t'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
    Images.append(a.img['src'])
   
# Storing scraped content
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings,'Image':Images})
df.to_csv('products.csv', index=False, encoding='utf-8')