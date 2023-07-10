def count(input_list):
    
    results = {}

    for element in set(input_list):
        results[element] = input_list.count(element)
    
    return results