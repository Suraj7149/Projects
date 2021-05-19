# function to select file and calculate the total number of words and return it.
def select_file():

    ''' select file, count words and returns it.'''

    # selection
    text_file = input("Enter the full path of File:- ")
    selected_file = open(text_file, "r")
    total_words = 0

    # counting
    for i in selected_file.read().split():
        total_words = total_words + 1
    
    # return
    print("Total Words are : ", total_words)

if __name__ == "__main__":
    select_file()
        
