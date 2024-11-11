"""
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
"""

#task1
class Node_lab:
    def __init__(self, data):
        self.data = data
        self.next = None

class Node_labList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node_lab(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Елемент {data} додано у список.")

    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f"Елемент {data} видалено з списку.")
                return
            previous = current
            current = current.next
        print(f"Елемент {data} не знайдено у списку.")

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Вміст списку:", elements)

    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                print(f"Значення {data} є у списку.")
                return True
            current = current.next
        print(f"Значення {data} немає у списку.")
        return False

    def replace(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                print(f"Значення {old_data} замінено на {new_data}.")
                return
            current = current.next
        print(f"Значення {old_data} не знайдено у списку.")

def main():
    linked_list = Node_labList()
    initial_data = input("Введіть початковий набір чисел через пробіл: ")
    for num in initial_data.split():
        linked_list.add(int(num))

    while True:
        print("\nМеню:")
        print("1. Додати елемент у список.")
        print("2. Видалити елемент зі списку.")
        print("3. Показати вміст списку.")
        print("4. Перевірити, чи є значення у списку.")
        print("5. Замінити значення у списку.")
        print("6. Вийти.")

        choice = input("Виберіть пункт: ")

        if choice == '1':
            data = int(input("Введіть число для додавання: "))
            linked_list.add(data)
        elif choice == '2':
            data = int(input("Введіть число для видалення: "))
            linked_list.delete(data)
        elif choice == '3':
            linked_list.display()
        elif choice == '4':
            data = int(input("Введіть число для перевірки: "))
            linked_list.contains(data)
        elif choice == '5':
            old_data = int(input("Введіть значення для заміни: "))
            new_data = int(input("Введіть нове значення: "))
            linked_list.replace(old_data, new_data)
        elif choice == '6':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

main()

#task2
class Node_lab2:
    def __init__(self, data2):
        self.data2 = data2
        self.next2 = None
        self.prev2 = None

