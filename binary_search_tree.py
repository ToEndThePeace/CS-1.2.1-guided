# NOT NEEDED!
# class BinarySearchTree:
#     def __init__(self, root=None):
#         self.root = root

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        text = f"{self.value}, "
        if self.left:
            text += str(self.left)
        if self.right:
            text += str(self.right)
        return text

    def insert(self, value):
        # 1. compare input value with value of the node
        # 2. if value < node value,
        # 		go left
        #		if there's no left child, wrap in node and park
        #		ELSE call THAT child's insert method
        # 3. if >=,
        # 		go right
        #		if there's no right child, wrap in node and park
        #		ELSE call THAT child's insert method
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        pass


root = BSTNode(26)
root.insert(12)
root.insert(10)
root.insert(27)
root.insert(13)
root.insert(1)
root.insert(193)
print(root)