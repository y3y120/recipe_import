import unittest
import recipe_import

AllR_URL = "https://www.allrecipes.com/recipe/269592/pork-chops-in-garlic-mushroom-sauce/"
test_title_AllR = "Pork Chops in Garlic Mushroom Sauce Recipe | Allrecipes"
test_directions_AllR    = [ 'Season both sides of pork chops with paprika, salt, and pepper.', 
                            'Heat a large skillet over medium-high heat; add 2 tablespoons butter. Sear pork chops until golden brown and no longer pink in the center, 2 to 4 minutes per side. Remove pork chops from the skillet and set aside.', 
                            'Melt remaining butter in the same skillet over medium-high heat. Add mushrooms and cook until golden and excess moisture evaporates, about 5 minutes. Add garlic and mustard; cook until garlic is fragrant, about 1 minute.', 
                            'Add flour to the skillet, stirring to remove any lumps. Slowly add beef broth, whisking until incorporated. Season with salt and pepper. Reduce heat to medium and simmer, stirring often, until sauce thickens, about 5 minutes. Check for seasoning again.', 
                            'Return pork chops to the skillet and cook until heated through, about 1 minute. Serve hot.']

test_ingredients_AllR=[ '2 pounds boneless pork chops ', 
                        '½ teaspoon paprika ', 
                        '1 pinch kosher salt and ground black pepper to taste ', 
                        '¼ cup butter, divided ', 
                        '1 (8 ounce) package sliced fresh mushrooms ', 
                        '4 cloves garlic, minced ', 
                        '1 teaspoon Dijon mustard ', 
                        '2 tablespoons all-purpose flour ', 
                        '2 cups beef broth '] 

class TestRturnMethods(unittest.TestCase):

    def test_return_ingredients(self):
        recipe = recipe_import.RecipeImport(AllR_URL)
        self.assertEqual(recipe.return_ingredients(), test_ingredients_AllR)

    def test_return_directions(self):
        recipe = recipe_import.RecipeImport(AllR_URL)
        self.assertEqual(recipe.return_directions(), test_directions_AllR)

    def test_return_title(self):
        recipe = recipe_import.RecipeImport(AllR_URL)
        self.assertEqual(recipe.return_title(), test_title_AllR)

if __name__ == '__main__':
    unittest.main()
