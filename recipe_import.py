import requests,re
from bs4 import BeautifulSoup

url = "https://automatetheboringstuff.com/chapter11/"
url2 = "https://www.allrecipes.com/recipe/269592/pork-chops-in-garlic-mushroom-sauce/"
url3 = "https://www.allrecipes.com/recipe/47247/chili-rellenos-casserole/"
url4 = "https://www.tasteofhome.com/recipes/cool-beans-salad/"
r = requests.get(url2)

soup = BeautifulSoup(r.text, 'html.parser')
title = soup.title.string



def return_title(soup):
    """ returns title string of Beautiful soup object site """
    title = soup.title.string
    return title


#TODO: Make this capture more than just stuff from All recipies
def return_ingredients(soup):
    """
    return_ingredients takes a BeatifulSoup object and parses through the html
    to find the ingredient list and returns a list of the string values of that 
    list.

    TODO: Only works with Allrecipes.com right now. Needs to be setup to work with 
    other sites
    """

    lists = soup.find_all(['ul'])
    section_match = re.compile('ingredients.*(section|body)')
    list_match = re.compile('ingredients.*name')
    ingredients = []
    ingredient_list = None
    for item in lists:
        if item.has_attr('class'):
            if re.search(section_match,str(item['class'])):
               ingredient_list = item.find_all('span')
               break
    for item in ingredient_list:
        if item.has_attr('class'):
            if re.search(list_match,str(item['class'])):
                ingredients.append(item.string)
    return ingredients

def return_directions(soup):
    """
    return_directions takes a BeatifulSoup object and parses through the html
    to find the ingredient list and returns a list of the string values of that 
    list.

    TODO: Only works with Allrecipes.com right now. Needs to be setup to work with 
    other sites
    """

    lists = soup.find_all(['ul'])
    section_match = re.compile('directions|instructions')
    list_match = re.compile('paragraph')
    directions = []
    direction_list = None
    for item in lists:
        if item.has_attr('class'):
            if re.search(section_match,str(item['class'])):
               direction_list = item.find_all('div')
               break
    for item in direction_list:
        if item.has_attr('class'):
            if re.search(list_match,str(item['class'])):
                directions.append(item.find('p').string)
    return directions 


#return_ingredients(soup)
#print(return_directions(soup))
