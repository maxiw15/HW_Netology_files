cook_book = {}
with open("recipes.txt", encoding="utf8") as file:
    for line in file:
        dish_name = line.strip()
        cook_book[dish_name] = []
        count = int(file.readline())
        for ingredients in range(count):
            ingredient_name, quantity, measure = file.readline().split(" | ")
            dish_names = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
            cook_book[dish_name].append(dish_names)
        file.readline()

for i in cook_book.items():
    print(i)





