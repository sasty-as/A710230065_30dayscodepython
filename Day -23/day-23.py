#  Abstraction pada OOP

class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.__items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)

    def __str__(self):
        return f"Stack({self.__items})"

# Contoh penggunaan kelas Stack yang sudah dikembangkan
s = Stack()
print(s.is_empty())  # Output: True

s.push(1)
s.push(2)
s.push(3)
print(s.peek())  # Output: 3
print(s.size())  # Output: 3

s.pop()
print(s.peek())  # Output: 2
print(s.size())  # Output: 2

print(s)  # Output: Stack([1, 2])
