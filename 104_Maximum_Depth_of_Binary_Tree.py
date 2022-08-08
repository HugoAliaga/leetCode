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
    def maxDepth(self, root) -> bool:
        def dfs(node,i,max_i):
            a1,a2 = 0,0
            if node != None and node.val != None:
                if node.left:
                    a1 = dfs(node.left,i+1,max_i)
                if node.right:
                    a2 = dfs(node.right,i+1,max_i)
            return max(a1,a2,max_i,i)
        
        return dfs(root,1,0)

tests = []
solutions = []
tests.append([3,9,20,None,None,15,7])
solutions.append([[3],[20,9],[15,7]])

tests.append([1])
solutions.append([[1]])

for i in range(len(tests)):
    tree = TreeNode()
    tree.fromArray(tests[i])
    ans = Solution().maxDepth(tree)
    print('T',i,'R',ans,solutions[i])