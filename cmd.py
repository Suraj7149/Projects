from mimetypes import init
import string
from timeit import repeat


class cmd_prompt():
        def __init__(self):
             pass
        def repeat(res):
            res = res.replace("repeat-", "")
            print(res)


if __name__ == "__main__":
    cmd = cmd_prompt()
    while(True):
        respond = input(">>>")
        if respond == "exit":
            break
        elif "repeat" in respond:
            
            cmd_prompt.repeat(respond)




    