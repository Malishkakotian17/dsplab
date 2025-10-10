
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current


    def delete(self, key):
        current = self.head

        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

        print(f"Value {key} not found.")


    def display(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


dll = DoublyLinkedList()
dll.insert(10)
dll.insert(20)
dll.insert(30)

print("Doubly Linked List:")
dll.display()

dll.delete(20)
print("After deleting 20:")
dll.display()
