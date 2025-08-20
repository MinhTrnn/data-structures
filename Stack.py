class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def is_empty(self):
        return self.top is None
    
    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.value, end = " -> ")
            current = current.next
        print("None")
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop")
            return None
        tmp = self.top
        self.top = self.top.next
        return tmp
    
    def peek(self):
        return self.top

def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    result = ""
    while stack.peek():
        result += stack.pop().value
    return result

if __name__ == "__main__":
#     stack = Stack()
#     stack.push(12)
#     stack.push(10)
#     stack.push(20)
#     stack.print_stack()
#     print(stack.peek().value)
#     print(stack.pop().value)
#     stack.print_stack()
    string = "hello, good morning"
    print(reverse_string(string))
    