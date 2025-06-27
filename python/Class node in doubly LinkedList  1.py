class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def insert_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = new_node
			new_node.prev = temp

dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)



def display_forward(self):
	temp = self.head
	print("Forward:")
	while temp:
		print(temp.data, end=" ")
		temp = temp.next
	print("None")

def display_backward(self):
	temp = self.head
	if temp is None:
		print("List is empty")
		return

	while temp.next:
		temp = temp.next
	print("Backward:")
	while temp:
		print(temp.data, end=" ")
		temp = temp.prev
	print("None")



def delete(self, value):
	temp = self.head
	while temp:
		if temp.data == value:
			if temp.prev:
				temp.prev.next = temp.next
			else:
				self.head = temp.next
			if temp.next:
				temp.next.prev = temp.prev
			return
		temp = temp.next



DoublyLinkedList.display_forward = display_forward
DoublyLinkedList.display_backward = display_backward
DoublyLinkedList.delete = delete

dll.insert_end(30)
dll.display_forward()
dll.display_backward()
dll.delete(20)
print("After deleting 20:")
dll.display_forward()

