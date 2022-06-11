class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Double_Linked_List:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("\n")
            print("Linked List is Empty.!!")
        else:
            itr = self.head
            print("\n")
            while itr:
                print(str(itr.data)+"-->"  if itr.next else str(itr.data), end=" ")
                itr = itr.next

    def rev_print(self):
        if self.head is None:
            print("\n")
            print("Linked List is Empty.!!")
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next

            print("\n")
            while itr:
                print(str(itr.data)+"-->"  if itr.prev else str(itr.data), end=" ")
                itr = itr.prev
                 
    def add_top(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next

            itr.next = new_node
            new_node.prev = itr

    def delete_begin(self):
        if self.head is None:
            print("\nDLL is empty.!!")
            return
        
        if self.head.next == None:
            self.head = None
            print("\nDLL is empty after deleting the node!.")
        else:
            self.head = self.head.next
            self.head.prev = None
            
    def delete_end(self):
            if self.head is None:
                print("DLL is empty can't delete!")

            if self.head.next == None:
                self.head = None
                print("DLL is Empty after deleting the node!")

            else:
                node = self.head
                while node.next:
                    node = node.next

                node.prev.next = None

            
    def delete_by_vaule(self, value):
        if self.head is None:
            print("DLL is empty.!!")

        if self.head.next is None:
            if value == self.head.data:
                self.head = None
            else:
                print(f"{value} is not present in the DLL.")
            return
        if self.head.data == value:
            self.head = self.head.next
            self.head.prev = None
            return
        node = self.head
        while node.next:
            if value == node.data:
                break
            node = node.next

            if node.next:
                node.next.prev = node.prev
                node.prev.next = node.next
            else:
                if node.data == value:
                    node.prev.next = None
                else:
                    print(f"{value} is not present in the DLL.")


if __name__ == "__main__":
    dll = Double_Linked_List()

    dll.delete_begin()

    dll.add_top(1)
    dll.delete_begin()

    dll.add_top(1)
    dll.add_top(2)
    dll.add_top(3)
    dll.add_top(4)
    dll.add_top(5)

    dll.print()
    dll.rev_print()

    dll.delete_begin()
    dll.delete_end()
    dll.delete_by_vaule(3)
    dll.print()

    
    

    
     

     