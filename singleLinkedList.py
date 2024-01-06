class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def is_empty(self):
        return self.head is None

    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        current = self.head
        print("Nodes of singly linked list:")
        while current is not None:
            print(current.data)
            current = current.next

    def delete_node(self, data):
        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                if current == self.tail:
                    self.tail = prev
            prev = current
            current = current.next
        print(f"Node with data {data} not found")

s_list = SinglyLinkedList()
s_list.add_node(1)
s_list.add_node(2)
s_list.add_node(3)
s_list.add_node(4)
s_list.display()
print("Deleting a node.")
s_list.delete_node(2)
s_list.display()
s_list.delete_node(5)