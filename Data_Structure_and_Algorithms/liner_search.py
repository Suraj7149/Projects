def linear_search(list, target):

    # Returns the index position of the target if found,
    # else returns None

    for i in range(0, len(list)):
        if list[i] == target:
            return i
        else:
            return None
         

if __name__ == "__main__":
    list1 = [12,32,45,65,56,78,90,100,24]
    print(linear_search(list1, 65))

