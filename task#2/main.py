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


def get_shop_list_by_dishes(dishes, person_count):
    """
    Функция принимает на вход список блюд и количество персон.
    А на выходе создаёт словарь с названием и количеством ингредиентов.
    """
    cook_book = reads_recipes()
    res = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in res:
                    res[ingredient['ingredient_name']] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    res[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
        else:
            print(f'Нет блюда: {dish}.')
    return res


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))