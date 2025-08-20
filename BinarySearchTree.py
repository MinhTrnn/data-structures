class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def inorder(self):
        self._inorder(self.root)
    
    def _inorder(self, root):
        if root is None:
            return
        self._inorder(root.left)
        print(root.value, end = " ")
        self._inorder(root.right)
        
    def insert(self, value):
        self.root = self._insert(value, self.root)
    
    def _insert(self, value, root):
        new_node = Node(value)
        if root is None:
            return new_node
        if value >= root.value:
            root.right = self._insert(value, root.right)
        else:
            root.left = self._insert(value, root.left)
        return root

    def search(self, key):
        return self._search(key, self.root)
    
    def _search(self, key, root):
        if root is None: # not found
            return False
        result = False
        if key < root.value:
            result = self._search(key, root.left)
        elif key > root.value:
            result = self._search(key, root.right)
        else: # key == value
            return True
        return result
    
    def validate(self):
        return self._validate(self.root, float("-inf"), float("inf"))
    
    def _validate(self, node, low, high):
        if node is None:
            return True
        # cho phép trùng ở nhánh phải => low <= value < high
        if not (low <= node.value < high):
            return False
        return (self._validate(node.left, low, node.value) and
                self._validate(node.right, node.value, high))
    


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(10)
    bst.insert(15)
    bst.insert(17)
    bst.insert(25)
    bst.insert(5)
    
    bst.inorder()
    print()
    print(bst.search(15))

    