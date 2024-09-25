def cookbook(*args):
    result = []
    dict_with_kitchen = {}
    dict_with_recipes = {}

    for recipe_name, kitchen, list_with_ingredients in args:
        if kitchen not in dict_with_kitchen:
            dict_with_kitchen[kitchen] = 0
        dict_with_kitchen[kitchen] += 1

        if kitchen not in dict_with_recipes:
            dict_with_recipes[kitchen] = []
        dict_with_recipes[kitchen].append((recipe_name, list_with_ingredients))

    sorted_cuisines = sorted(dict_with_kitchen.items(), key=lambda x: (-x[1], x[0]))

    for cuisine, count in sorted_cuisines:
        result.append(f'{cuisine} cuisine contains {count} recipes:')
        recipes = sorted(dict_with_recipes[cuisine], key=lambda x: x[0])
        for recipe_name, ingredients in recipes:
            ingredient_list = ', '.join(ingredients)
            result.append(f'  * {recipe_name} -> Ingredients: {ingredient_list}')



    return "\n".join(result)

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))


