def count(input_list):
    
    unique_list = []
    results = {}

    for letter in input_list:
        if letter not in unique_list:
            unique_list.append(letter)
        else:
            continue
    
    for element in unique_list:
        results[element] = input_list.count(element)
    
    return results