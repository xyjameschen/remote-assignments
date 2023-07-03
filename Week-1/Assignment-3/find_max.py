def find_max(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    else:
        max_value = numbers[0]
        for index in range(1, len(numbers)):
            if max_value >= numbers[index]:
                continue
            else:
                max_value = numbers[index]
        return max_value