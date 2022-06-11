# binary search system 

from importlib import import_module


def binary_search(array, item,high, low = 0):
    mid = int((high + low)/2)
    
    if array[mid] == item:
        return f"Element found at: {mid}"
    elif array[mid] < item:
        return binary_search(array, item, low=(mid + 1))
    elif array[mid] > item:
        return binary_search(array, item,high=(mid-1))
    else:
        return f"Element cannot be found."

if __name__ == "__main__":
    binary_list = []
    total_element = int(input("Total number of Elements in the array are:- "))
    for i in range(0, total_element):
        element = input(f"Enter the element No. {i}: ") 
        binary_list.append(element)

    item = input("Enter the element to be searched: ")

    binary_search(binary_list,item, high=len(binary_list))      




