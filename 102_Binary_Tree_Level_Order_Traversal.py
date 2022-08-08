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
    def levelOrder(self, root) -> bool:
        ans = []
        def dfs(node,i):
            if node != None and node.val != None:
                if len(ans)<i:
                    ans.append([])
                ans[i-1].append(node.val)
            if node.left:
                dfs(node.left,i+1)
            if node.right:
                dfs(node.right,i+1)
        dfs(root,1)
        return ans

tests = []
solutions = []
tests.append([0,2,4,1,None,3,-1,5,1,None,6,None,8])
solutions.append([[0],[2,4],[1,3,-1],[5,1,6,8]])
tests.append([3,9,20,None,None,15,7])
solutions.append([[3],[9,20],[15,7]])

tests.append([1])
solutions.append([[1]])

for i in range(len(tests)):
    tree = TreeNode()
    tree.fromArray(tests[i])
    ans = Solution().levelOrder(tree)
    print('T',i,'R',ans,solutions[i])