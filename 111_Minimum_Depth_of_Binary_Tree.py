from xmlrpc.client import MAXINT


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
        if array: self.val = array[0]
        else: return None


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
            if self.val != None:
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
    def minDepth(self, root) -> bool:
        
        def dfs2(node,idx):
            if not node: return idx-1
            left, right = False,False
            if node.left: left = dfs(node.left,idx+1)
            if node.right: right = dfs(node.right,idx+1)
            if not left and not right: return idx
            if not left: return right
            if not right: return left
            return min(left,right)
        
        if not root: return 0
        d = list(map(self.minDepth, (root.left, root.right)))
        return 1 + (min(d) or max(d))
tests = []
solutions = []

tests.append([3,9,20,None,None,15,7])
solutions.append(2)

tests.append([2,None,3,None,4,None,5,None,6])
solutions.append(5)

tests.append([])
solutions.append(0)



for i in range(len(tests)):
    tree1 = TreeNode()
    tree1.fromArray(tests[i])
    ans = Solution().minDepth(tree1)
    print('T',i,'R',ans,solutions[i])