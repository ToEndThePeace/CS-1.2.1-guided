# NOT NEEDED!
# class BinarySearchTree:
#     def __init__(self, root=None):
#         self.root = root
from collections import deque


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

    def iterative_depth_first_foreach(self, fn):
        # last in first out
        stack = []
        stack.append(self)

        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)
            fn(current.value)

    def iterative_breadth_first_foreach(self, fn):
        # first in first out -> queue
        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            fn(current.value)
        pass


root = BSTNode(26)
root.insert(12)
root.insert(10)
root.insert(27)
root.insert(13)
root.insert(1)
root.insert(193)
print(root)
