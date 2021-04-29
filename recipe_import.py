import requests,re
from bs4 import BeautifulSoup

url = "https://automatetheboringstuff.com/chapter11/"
url2 = "https://www.allrecipes.com/recipe/269592/pork-chops-in-garlic-mushroom-sauce/"
r = requests.get(url2)

soup = BeautifulSoup(r.text, 'html.parser')

for header in soup.find_all('h1'):
    print(header)
    if re.search("Ingredient", str(header)):
        print(header)

for header in soup.find_all('h2'):
    if re.search("Ingredients", str(header.string)):
        print(header.string)
