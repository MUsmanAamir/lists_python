def sumArray(arr:list)->int:
    sum:int = 0
    for num in arr:
        sum = sum + num
    return sum

numbers:list = [2,4,5,6,7,8]
sum = sumArray(numbers)
print(f"The sum of all number in list:  {sum}")