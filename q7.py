def sumArray(arr: list) -> int:
    total = 0
    index = 0
    while index < len(arr):  
        total = total + arr[index]  
        index += 1 
    return total

numbers = [2, 4, 5, 6, 7, 8]
sum_result = sumArray(numbers)
print(f"The sum of all numbers in the list: {sum_result}")
