import easygui

path = easygui.fileopenbox()

string1 = " " 
for i in range(1, len(path)):
    if path[-i] == "/":
        break
    else:
        string1 = string1+(path[-i])
        continue
    
print(string1[::-1])