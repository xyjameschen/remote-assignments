def avg(products_dic):

    total = len(products_dic['products'])
    price_list = []

    for dic in products_dic['products']:
        price_list.append(dic['price'])
    
    results = round((sum(price_list) / total), 3)
    return results