class MaxHeap:
    def __init__(self, capacity):
        self.heap = (capacity + 1) * [None]
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def printHeap(self):
        for i in range(self.size + 1):
            print(self.heap[i], end=" ")
        print()
    
    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(len(self.heap)):
            new_array[i] = self.heap[i]
        self.heap = new_array
            
    def insert(self, value):
        if self.size == len(self.heap) - 1:
            self.resize(self.size * 2)
        self.size += 1
        self.heap[self.size] = value
        self.swim(self.size)
    
    def swim(self, k):
        while k > 1 and self.heap[k] > self.heap[k//2]:
            self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k = k//2
    
    def delete(self):
        tmp = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.sink(1)
        return tmp
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def sink(self, k):
        # has at least 1 child
        while 2*k <= self.size:
            # has 1 child:
            if 2*k == self.size:
                if self.heap[k] < self.heap[2*k]:
                    self.swap(k, 2*k)
                    k = 2*k
                else:
                    break
            # has 2 children
            else:
                if self.heap[2*k] > self.heap[2*k + 1]:
                    if self.heap[2*k] > self.heap[k]:
                        self.swap(k, 2*k)
                        k = 2*k
                    else:
                        break
                else:
                    if self.heap[2*k + 1] > self.heap[k]:
                        self.swap(k, 2*k + 1)
                        k = 2*k + 1
                    else:
                        break
            
                    
if __name__ == "__main__":
    maxHeap = MaxHeap(5)
    print(maxHeap.is_empty())
    maxHeap.insert(20)
    maxHeap.insert(10)
    maxHeap.insert(30)
    maxHeap.insert(15)
    maxHeap.insert(40)
    maxHeap.insert(35)
    
    maxHeap.printHeap()
    
    maxHeap.delete()
    maxHeap.printHeap()
    
