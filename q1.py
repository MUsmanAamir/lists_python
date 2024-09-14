def insertElement(arr: list, index: int, value: int) -> list:
    arr.insert(index, value)
    return arr

elements: list = [1, 2, 3, 4, 5]
print("List before insertion:\n", elements)
elements = insertElement(elements, 2, 11)
print("List after insertion:\n", elements)