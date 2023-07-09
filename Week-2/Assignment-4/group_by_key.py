def group_by_key(input_list):
    
    unique_keys = []
    results_dic = {}
    
    for dic in input_list:
        if dic['key'] not in unique_keys:
            unique_keys.append(dic['key'])
        else:
            continue
    
    for letter in unique_keys:
        total = 0
        for dic in input_list:
            if letter == dic['key']:
                total += dic['value']
            else:
                continue
        results_dic[letter] = total
    
    return results_dic
