from math import ceil


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def fromArray(self,array):
        ln = len(array)
        def helper(n):
            if n >= ln or array[n]==None:
                return None
            root = TreeNode(array[n])
            root.left = helper(2*n+1)
            root.right = helper(2*n+2)
            return root
        self.left = helper(1)
        self.right = helper(2)
        self.val = array[0]


    def add(self, val, node):
        if not val: 
            self.val = val
            return True
        elif not self.left:
            self.left = TreeNode(val)
        elif not self.right:
            self.right = TreeNode(val)  

    def toArray(self):
        endArray = []
        if self != None:
            if self.val:
                endArray.append(self.val)
            if self.left: endArray += self.left.toArray()
            if self.right: endArray += self.right.toArray()
        return endArray

    def insert(self,value):
        if not self.val:
            self.val = value
        elif value > self.val:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        elif value < self.val:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)

class Solution:
    def recoverTree(self, root) -> None:
        in_order = []
        def inOrder(node):
            if node is None:
                return
            inOrder(node.left)
            in_order.append(node)
            inOrder(node.right)
        
        inOrder(root)

        sorted_order = sorted(in_order, key=lambda x:x.val)
        for i in range(len(in_order)):
            if in_order[i] != sorted_order[i]:
                in_order[i].val, sorted_order[i].val = sorted_order[i].val, in_order[i].val
                return root

tests = []
solutions = []

tests.append([1,3,None,None,2])
solutions.append([3,1,None,None,2])

tests.append([3,1,4,None,None,2])
solutions.append([2,1,4,None,None,3])

for i in range(len(tests)):
    tree_el = TreeNode()
    tree_el.fromArray(tests[i])
    ans = Solution().recoverTree(tree_el)
    print('T',i,'R',ans.toArray(),solutions[i])