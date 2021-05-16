selected_file = open("D:\\text.txt", "r")
total_words = 0
for i in selected_file.read().split():
    total_words = total_words + 1
    print("Total Words are : ", total_words)