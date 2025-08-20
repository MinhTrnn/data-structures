class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def pre_order_recursive(self, root):
        if root is None: # base case
            return
        print(root.value, end = " ")
        self.pre_order_recursive(root.left)
        self.pre_order_recursive(root.right)
    
    def pre_order_iterative(self):
        stack = []
        stack.append(self.root)
        while stack:
            tmp = stack.pop()
            print(tmp.value, end =" ")
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
    
    def in_order_recursive(self, root):
        if root is None:
            return
        self.in_order_recursive(root.left)
        print(root.value, end = " ")
        self.in_order_recursive(root.right)
    
    def post_order_recursive(self, root):
        if root is None:
            return
        self.post_order_recursive(root.left)
        self.post_order_recursive(root.right)
        print(root.value, end = " ")
    
    def level_order(self):
        queue = []
        queue.append(self.root)
        while queue:
            tmp = queue.pop(0)
            print(tmp.value, end = " ")
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
    
    def find_max(self, root):
        if root is None:
            return float('-inf')
        left_max = self.find_max(root.left)
        right_max = self.find_max(root.right)
        return max(root.value, left_max, right_max)

if __name__ == "__main__":
    bt = BinaryTree()
    one = Node(10)
    two = Node(5)
    three = Node(7)
    four = Node(4)
    five = Node(6)
    six = Node(3)
    bt.root = one
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.right = six
    bt.level_order()
    print()
    print(bt.find_max(bt.root))
    
    