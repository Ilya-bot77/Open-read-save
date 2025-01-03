cook_book = {}

# функция перевода текста из файла в словарь
def dict_cook_book(self):
    with open(self, encoding='utf-8') as f:
        for line in f:
            dish = line.strip()
            count = int(f.readline())
            ingredient_list = []
            for ing in range(count):
                ingredient_dict = {}
                item1, item2, item3 = f.readline().split(" | ")
                ingredient_dict["ingredient_name"] = item1.strip()
                ingredient_dict["quantity"] = int(item2.strip())
                ingredient_dict["measure"] = item3.strip()
                ingredient_list.append(ingredient_dict)
            cook_book[dish] = ingredient_list
            f.readline()

dict_cook_book("1.txt")
print(cook_book)