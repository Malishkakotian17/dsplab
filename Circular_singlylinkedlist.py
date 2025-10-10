from colorama import Fore, Back, Style, init

init(autoreset=True)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node
        print(Fore.GREEN + "Node inserted at the beginning" + Style.RESET_ALL)

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        print(Fore.GREEN + "Node inserted at the end" + Style.RESET_ALL)

    def insert_at_position(self, data, position):
        if position <= 0:
            print(Fore.RED + "position should be >= 1" + Style.RESET_ALL)
            return
        new_node = Node(data)
        if position == 1:
            self.insert_at_beginning(data)
            return
        temp = self.head
        count = 1
        while count < position - 1 and temp.next != self.head:
            temp = temp.next
            count += 1
        if count < position - 1:
            print(Fore.RED + "position out of range" + Style.RESET_ALL)
            return
        new_node.next = temp.next
        temp.next = new_node
        print(Fore.GREEN + "Node inserted at position " + str(position) + Style.RESET_ALL)


    def display(self):
        if self.head is None:
            print(Fore.BLUE + "List is empty" + Style.RESET_ALL)
            return
        temp = self.head
        while True:
            print(Fore.BLUE + str(temp.data) + Style.RESET_ALL, end="->")
            temp = temp.next
            if temp == self.head:
                break
        print(Fore.BLUE + "(head)" + Style.RESET_ALL)
    

circular_sll = CircularSinglyLinkedList()
circular_sll.insert_at_end(10)
circular_sll.insert_at_beginning(5)
circular_sll.insert_at_position(7, 2)
circular_sll.display()
circular_sll.insert_at_position(15, 5)  # This should show "position out of range"
circular_sll.display()
