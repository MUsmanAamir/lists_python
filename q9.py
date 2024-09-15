def removeOdd(arr:list)->list:
    odds = []
    for num in arr:
        if(num%2==0):
            odds.append(num)
        
    return odds

arr:list = [1,2,3,4,5,6,7,8,9,10]
evens:list = removeOdd(arr)
print(f"List without odd numbers: {evens}")