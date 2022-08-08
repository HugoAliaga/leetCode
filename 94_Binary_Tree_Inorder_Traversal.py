
from math import ceil, floor

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def fromArray(self,array):
        if array:
            self.val = array[0]
            array_div = array[1:]
            if array_div:
                if array_div[0] == None:
                    self.left = TreeNode()
                    self.left.fromArray([None])
                    self.right = TreeNode()
                    self.right.fromArray(array_div[1:])
                elif len(array_div)>1 and array_div[1]==None:
                    self.left = TreeNode()
                    self.left.fromArray(array_div[:1]+array_div[2:])
                    self.right = TreeNode()
                    self.right.fromArray([None])
                else:
                    ln = ceil(len(array_div)/2)
                
                    array_left = array_div[:ln]
                    array_right = array_div[ln:]

                    if array_left:
                        self.left = TreeNode()
                        self.left.fromArray(array_left)
                    if array_right:
                        self.right = TreeNode()
                        self.right.fromArray(array_right)

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

class Solution:
    def inorderTraversal(self, root):
        ans = []
        def traverse(node):
            if node != None:
                if node.left: traverse(node.left)
                if node.val != None: ans.append(node.val)
                if node.right: traverse(node.right)
        traverse(root)
        return ans

tests = []
solutions = []

tests.append([1,None,2,3])
solutions.append([1,3,2])

tests.append([])
solutions.append([])

tests.append([1])
solutions.append([1])

for i in range(len(tests)):
    val = TreeNode()
    val.fromArray(tests[i])
    ans = Solution().inorderTraversal(val)
    print('T',i,ans,solutions[i])