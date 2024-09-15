
def convertTemp(cels:list)->list:
   
    fah = []
    for i in cels:
        f = (i*9/5)+32 
        fah.append(f"{f}F")
    return fah

fahrens =[]
n = int(input("Enter the number of temperatures you want to enter: "))
for i in range(n):
    i = int(input(f"Enter Temperature{i+1}: "))
    fahrens.append(i)

result = convertTemp(fahrens)
print(f"List after conversion: {result}")

            