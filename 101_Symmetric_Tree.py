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
    def isSymmetric(self, root) -> bool:

        def dfs(node1,node2):
            if not node1: return not node2
            if not node2: return not node1
            return node1.val == node2.val and dfs(node1.left,node2.right) and dfs(node1.right,node2.left)
            
        return dfs(root.left,root.right)

tests = []
solutions = []

tests.append([1,2,2,3,4,4,3])
solutions.append(True)

tests.append([1,2,2,None,3,None,3])
solutions.append(False)

for i in range(len(tests)):
    tree = TreeNode()
    tree.fromArray(tests[i])
    ans = Solution().isSymmetric(tree)
    print('T',i,'R',ans,solutions[i])