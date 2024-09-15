def factorial(num: int) -> int:
    result = 1
    while num > 1:
        result = result * num
        num -= 1
    return result

number = int(input("Enter a positive integer: "))
print(f"The factorial of {number} is {factorial(number)}")
