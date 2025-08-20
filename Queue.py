class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def is_empty(self):
        return self.front is None
    
    def print_queue(self):
        current = self.front
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue")
            return None
        elif self.length == 1:
            tmp = self.front
            self.front = self.rear = None
            self.length -= 1
            return tmp
        tmp = self.front
        self.front = self.front.next
        self.length -= 1
        return tmp
    
    def front(self):
        return self.front

def print_binary(n):
    queue = Queue()
    queue.enqueue("1")
    for i in range(n):
        c = queue.dequeue().value
        print(c, end = " ")
        queue.enqueue(c + "0")
        queue.enqueue(c + "1")
    

if __name__ == "__main__":
#     queue = Queue()
#     queue.enqueue(12)
#     queue.enqueue(18)
#     queue.enqueue(7)
#     print(queue.dequeue().value)
#     print(queue.dequeue().value)
#     queue.print_queue()
    print_binary(10)
    