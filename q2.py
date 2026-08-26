def process_list(numbers):
    result = numbers.copy()

    i = 0
    while i < len(result):
        if result[i] < 0:
            result.remove(result[i])
        else:
            i = i + 1

    result.append(0)
    result.sort()

    return result
original = [5, -2, 8, -1, 3]
result = process_list(original)
print("Original:", original)
print("Result:", result)