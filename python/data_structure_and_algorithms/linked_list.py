class Node:
    def __init__(self, data=None, ref=None):
        self.data = data
        self.ref = ref

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_top(self, data):
        node = Node(data, self.head)
        self.head = node

    def look(self):
        if self.head is None:
            print("The list is empty.")
            return

        #iterator 
        itr  = self.head

        while itr:
            print(str(itr.data) + "-->" if itr.ref else str(itr.data))
            itr = itr.ref
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)

        itr = self.head
        while itr.ref:
            itr = itr.ref

        itr.ref = Node(data, None)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.ref

        return count

    def del_by_value(self, x):
        if self.head == None:
            print("The Linked List is empty.!!")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present.")
        else:
            n.ref = n.ref.ref            
        
        




if __name__ == "__main__":
    ll = Linked_List()
    # ll.look()
    # ll.insert_at_top(1)
    # ll.insert_at_top(2)
    # ll.insert_at_top(3)
    # ll.insert_at_top(4)
    # ll.insert_at_top(5)
    # ll.insert_at_top(6)
    # ll.insert_at_top(7)
    # ll.insert_at_top(8)
    # ll.insert_at_top(9)
    # ll.insert_at_end(10)
    # ll.look()
    # ll.get_length()
    # ll.del_by_value(5)
    # ll.del_by_value(4)
    # ll.del_by_value(20)
    # ll.look()
    # ll.get_length()

    loop = True
    while loop:
        ask = input(">>>")

        if ask.lower() == "look":
            ll.look()

        if "topadd" in ask.lower():
            
            ask = ask.replace("topadd", "")
            ask = ask.replace("(","")
            ask = ask.replace(")","")
            ask = ask.replace("[", "")
            ask = ask.replace("]", "")
                
            for i in ask.split(","):
                ll.insert_at_top(i)

        if "endadd" in ask.lower():
            
            ask = ask.replace("endadd", "")
            ask = ask.replace("(","")
            ask = ask.replace(")","")
            ask = ask.replace("[", "")
            ask = ask.replace("]", "")
                
            for i in ask.split(","):
                ll.insert_at_end(i)

        if  "dlv" in ask.lower():
            ask = ask.replace("dlv", "")
            ask = ask.replace("(","")
            ask = ask.replace(")","")
            ask = ask.replace("[", "")
            ask = ask.replace("]", "")

            ll.del_by_value(ask)

        if ask.lower() == "exit":
            loop = False

