from colorama import Fore, Back, Style

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

        print(Fore.GREEN + "Node appended" + Style.RESET_ALL)

    def display(self):
        if not self.head:
            print(Fore.RED + "List is empty" + Style.RESET_ALL)
            return
        temp = self.head
        while True:
            print(Fore.BLUE + str(temp.data) + Style.RESET_ALL, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")
    
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.display()

        
