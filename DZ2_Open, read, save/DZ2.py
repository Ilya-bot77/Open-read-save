with open('1.txt', encoding='utf-8') as f:
    cook_book = {}
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
    # print(cook_book)

def get_shop_list_by_dishes(self, person_count):
    ingred_dict = {}
    for a in self:
        for key in cook_book:
            if key == a:
                for b in cook_book[key]:
                    new_dict_ingred = {}
                    ingredient = b["ingredient_name"]
                    new_dict_ingred["measure"] = b["measure"]
                    new_dict_ingred["quantity"] = b["quantity"] * person_count
                    ingred_dict[ingredient] = new_dict_ingred
    print(ingred_dict)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)