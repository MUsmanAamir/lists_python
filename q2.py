def addCart(arr: list, itemName: str) -> list:
    arr.append(itemName)
    return arr

def removeCart(arr: list, itemName: str) -> list:
    if itemName in arr:
        arr.remove(itemName)
    else:
        print(f"{itemName} not found in cart.")
    return arr

def updateCart(arr: list, itemName: str, newItemName: str) -> list:
    if itemName in arr:
        index = arr.index(itemName)
        arr[index] = newItemName
    else:
        print(f"{itemName} not found in cart.")
    return arr

def displayCart(arr: list):
    print("Current cart:")
    if len(arr) == 0:
        print("The cart is empty.")
    else:
        for item in arr:
            print(f"{item}")

arr = []

while True:
    print("\nShopping Cart")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Update item in cart")
    print("4. Display items in cart")
    print("5. Exit Program")

    choice = int(input("Choose a number: "))

    if choice == 1:
        item = input("Enter the name of the item: ")
        arr = addCart(arr, item)
        print(f"{item} added to cart.")
        displayCart(arr)

    elif choice == 2:
        item = input("Enter the name of the item to remove: ")
        arr = removeCart(arr, item)
        displayCart(arr)

    elif choice == 3:
        oldItem = input("Enter the name of the item to update: ")
        newItem = input("Enter the new name of the item: ")
        arr = updateCart(arr, oldItem, newItem)
        displayCart(arr)

    elif choice == 4:
        displayCart(arr)

    elif choice == 5:
        print("Exiting Program.")
        break

    else:
        print("Invalid option. Please choose a valid option.")
