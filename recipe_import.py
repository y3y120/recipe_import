import requests,re
from bs4 import BeautifulSoup

url = "https://automatetheboringstuff.com/chapter11/"
url2 = "https://www.allrecipes.com/recipe/269592/pork-chops-in-garlic-mushroom-sauce/"
url3 = "https://www.allrecipes.com/recipe/47247/chili-rellenos-casserole/"
r = requests.get(url3)

soup = BeautifulSoup(r.text, 'html.parser')
title = soup.title.string

def find_ingredients_section(soup):
    elements= soup.find_all(['ul'])
    for e in elements:
        if e.has_attr('class'):
            if re.search("ingredients",str(e['class'])):
                return e


def parse_ingredient_list(ingredients):
    ret = []
    ingredient = ingredients.find_all('span')
    for item in ingredient:
        if item.has_attr('class'):
            if re.search("name",str(item['class'])):
                ret.append(str(item.string))
    return ret

section = find_ingredients_section(soup)
ingredients = parse_ingredient_list(section)

print(title)
print( '\tIngredients:')
for i in ingredients:
    print('\t' + i)

