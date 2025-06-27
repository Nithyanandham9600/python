# Singly Linked List

# Insertion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    
    # Deletion

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    # Sorting

    def sort_list(self):
        if not self.head:
            return
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

    #  Swap Two Nodes

    def swap(self, x, y):
        if x == y:
            return
        a = self.head
        b = self.head
        while a and a.data != x:
            a = a.next
        while b and b.data != y:
            b = b.next
        if a and b:
            a.data, b.data = b.data, a.data
            