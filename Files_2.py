with open('recipes.txt', encoding='utf-8') as file:

    cook_book = {}

    def dicts():
        f = file.readline().strip()
        if f == '':
            f = file.readline().strip()
            if f == '': return
        title = f
        # print(title)
        n_str = file.readline().strip()
        for n in range(int(n_str)):
            string = file.readline().strip().split('|')
            # print(string)
            if title in cook_book:
                cook_book[title] += [{'ingredient_name': string[0], 'quantity': string[1], 'measure': string[2]}]
            else: cook_book[title] = [{'ingredient_name': string[0], 'quantity': string[1], 'measure': string[2]}]
        dicts()

    def func_print():
        dicts()
        # try: person_count = int(input("Введите количество персон: "))
        # except: func_print()
        # print(cook_book)
        # print()
        for recipes in cook_book.items():
            for recipe in recipes:
                print(recipe)
        shop_list_dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)
        print()
        print(shop_list_dict)


    def get_shop_list_by_dishes(dishes, person_count):
        ingredients = []
        for dish in dishes:
            if dish in cook_book:
                ingredients += cook_book[dish]
        shop_list_dict = {}
        for i in ingredients:
            if list(i.values())[0] in shop_list_dict:
                sum_quant = shop_list_dict[list(i.values())[0]]['quantity'] + (int(list(i.items())[1][1]) * person_count)
                shop_list_dict[list(i.values())[0]] = {list(i.items())[2][0]: list(i.items())[2][1], list(i.items())[1][0]: sum_quant}
            else: shop_list_dict[list(i.values())[0]] = {list(i.items())[2][0]: list(i.items())[2][1], list(i.items())[1][0]: int(list(i.items())[1][1]) * person_count}
        return shop_list_dict

    func_print()





