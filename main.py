def recipe_book(file_name, start_point=0):
    dictionary = {}
    with open(file_name, encoding="utf8") as file:
        file.seek(start_point)
        name = file.readline().replace("\n", "")
        dictionary[name] = []
        count = file.readline()
        for i in range(int(count)):
            ingredient_name, quantity, measure = file.readline().replace("\n", "").split(" | ")
            dictionary[name].append({"ingredient_name": ingredient_name})
            dictionary[name].append({"quantity": quantity})
            dictionary[name].append({"measure": measure})
        file.readline()
        stop_point = file.tell()
        if stop_point == file.seek(0, 2):
            return dictionary, -1
        else:
            return dictionary, stop_point


def main():
    answer = []
    temp, point = recipe_book("recipes.txt")
    answer.append(temp)
    while point != -1:
        temp, point = recipe_book("recipes.txt", point)
        answer.append(temp)
    return answer


print(main())
