def removeNegative(arr: list) -> list:
    result = []  
    for num in arr:
        if num >= 0:
            result.append(num)  
    return result

arr = [1, 2, 3, 4, -5, 5, 6, 7]

print(removeNegative(arr))
