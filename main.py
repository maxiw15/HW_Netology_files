def recipe_book():
    with open("recipes.txt", encoding="utf8") as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            cook_book[dish_name] = []
            count = int(file.readline())
            for ingredients in range(count):
                ingredient_name, quantity, measure = file.readline().split(" | ")
                dish_names = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                cook_book[dish_name].append(dish_names)
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    with open("recipes.txt", encoding="utf8") as file:
        for line in file:
            dish_name = line.strip()
            if dish_name in dishes:
                count = int(file.readline())
                for ingredients in range(count):
                    ingredient_name, quantity, measure = file.readline().split(" | ")
                    shop_list[ingredient_name] = []
                    if ingredient_name in shop_list:
                        ingredients_names = {'measure': measure.strip(), 'quantity': (int(quantity) * person_count)}
                        shop_list[ingredient_name].append(ingredients_names)
                    else:
                        ingredients_names += {'quantity': (int(quantity) * person_count)}
                        shop_list[ingredient_name].append(ingredients_names)
                file.readline()
        return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))