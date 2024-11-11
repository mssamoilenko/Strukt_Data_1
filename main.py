class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def delete(self, del_data):
        current = self.head
        if current and current.data == del_data:
            self.head = current.next
            return
        k = None
        while current and current.data != del_data:
            k = current
            current = current.next
        if current is None:
            return
        k.next = current.next

sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(4)
sll.display()
sll.delete(2)

sll.display()

class Node_2:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

dll = DoublyLinkedList()

dll.append(7)
dll.append(8)
dll.append(7)
dll.append(9)
dll.append(10)

dll.display()

class Node3:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        new_node = Node3(data)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if not self.top:
            return None
        data = self.top.data
        self.top = self.top.next
        return data
    def display(self):
        current = self.top
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

stack = Stack()
stack.push(4)
stack.push(7)
stack.push(9)
stack.push(5)
stack.push(3)
stack.display()
print(stack.pop())
stack.display()
