class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        current = self.head
        while current is not None:
            print(current.value, end = " -> ")
            current = current.next
        print("None")
    
    def find_length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, value):
        if self.head is None: #empty linked list
            self.insert_at_beginning(value)
            return
        new_node = Node(value)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    
    def insert_at_position(self, value, position):
        if self.head is None or position <= 0:
            self.insert_at_beginning(value)
            return
        if position > self.find_length():
            self.insert_at_end(value)
            return
        new_node = Node(value)
        count = 0
        current = self.head
        while count < position - 1:
            current = current.next
            count += 1
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty. Cannot delete")
            return None
        tmp = self.head
        self.head = self.head.next
        return tmp
    
    def delete_at_end(self):
        if self.head is None:
            print("List is empty. Cannot delete")
            return None
        if self.head.next is None: # list has 1 node
            tmp = self.head
            self.head = self.head.next
            return tmp
        current = self.head
        while current.next.next is not None:
            current = current.next
        tmp = current.next
        current.next = None
        return tmp
    
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty. Cannot delete")
            return None
        if position <= 0:
            self.delete_at_beginning()
            return None
        if position >= self.find_length():
            self.delete_at_end()
            return None
        current = self.head
        count = 0
        while count < position -1:
            current = current.next
            count += 1
        current.next = current.next.next
        

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_beginning(5)
    sll.insert_at_beginning(8)
    sll.insert_at_beginning(2)
    sll.insert_at_end(10)
    sll.insert_at_end(12)
    sll.insert_at_position(1, 2)
    sll.insert_at_position(7, 4)
    sll.insert_at_position(11, 7)
    sll.insert_at_position(20, 0)
    sll.delete_at_beginning()
    sll.delete_at_beginning()
    sll.delete_at_end()
    sll.delete_at_end()
    sll.delete_at_position(2)
#     sll.delete_at_position(0)
    sll.traversal()
    
    sll2 = SinglyLinkedList()
    sll2.insert_at_end(5)
    sll2.delete_at_end()
    sll2.traversal()
    
    