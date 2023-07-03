def find_position(numbers, target):
    if len(numbers) > 0:
        for index in range(len(numbers)):
            if numbers[index] == target:
                return index
            else:
                continue
        return -1
    else:
        return -1
