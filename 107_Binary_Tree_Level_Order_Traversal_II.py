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
    def levelOrderBottom(self, tree) -> bool:
        ans = []
        def dfs(tree,idx):
            if not tree: return
            if len(ans)<idx:
                ans.append([])
            ans[idx-1].append(tree.val)
            if tree.left: dfs(tree.left,idx+1)
            if tree.right: dfs(tree.right,idx+1)
        dfs(tree,1)
        return ans[::-1]
tests = []
solutions = []

tests.append([3,9,20,None,None,15,7])
solutions.append([[15,7],[9,20],[3]])


tests.append([[-1]])
solutions.append([-1])

tests.append([])
solutions.append([])

for i in range(len(tests)):
    new_tree = TreeNode()
    new_tree.fromArray(tests[i])
    ans = Solution().levelOrderBottom(new_tree)
    print('T',i,'R',ans,solutions[i])