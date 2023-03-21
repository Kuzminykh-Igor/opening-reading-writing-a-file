from pprint import pprint

def reads_recipes():
    """Функция парсит файл 'recipes.txt' в словарь cook_book"""
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredients_count = int(file.readline())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append(
                    {'ingredient_name': ingredient_name,
                     'quantity': int(quantity),
                     'measure': measure}
                )
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book


pprint(reads_recipes(), sort_dicts=False)