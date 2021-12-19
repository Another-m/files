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

    dicts()
    # print(cook_book)
    # print()
    for recipes in cook_book.items():
        for recipe in recipes:
            print(recipe)



