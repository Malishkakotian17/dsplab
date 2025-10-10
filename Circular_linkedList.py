class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None


    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def delete(self, key):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        prev = None

        if current.data == key:
            if current.next == self.head:
                self.head = None
                return

            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        prev = self.head
        current = self.head.next
        while current != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print(f"Value {key} not found.")


    def display(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")


cll = CircularLinkedList()
cll.insert(10)
cll.insert(20)
cll.insert(30)

print("Circular Linked List:")
cll.display()

cll.delete(20)
print("After deleting 20:")
cll.display()
