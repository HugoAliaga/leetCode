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
        if ln>1:
            self.left = helper(1)
        if ln>2:
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
        endArray.append(self.val)
        if self.left or self.right: 
            if self.left: endArray += self.left.toArray()
            else: endArray += [None]
            if self.right: endArray += self.right.toArray()
            else: endArray += [None]
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
    def maxPathSum(self, root) -> int:

        def dfs(node):            
            if not node: return 0
            left,right,arch1,arch2 = None, None, None, None
            if node.left: 
                left,arch1 = dfs(node.left)
            if node.right: 
                right,arch2 = dfs(node.right)
            this_arch = node.val
            this_line = node.val
            if left: 
                this_arch=max(this_arch,this_arch+left)
                this_line=max(this_line,node.val+left)
            if right: 
                this_arch=max(this_arch,this_arch+right)
                this_line = max(this_line,node.val+right)
            if arch1: this_arch = max(this_arch,arch1)
            if arch2: this_arch = max(this_arch,arch2)
            return this_line, this_arch
        ans = dfs(root)
        return max(ans[0],ans[1])

tests = []
solutions = []

tests.append([-1,-2,10,-6,None,-3,-6])
solutions.append(10)

tests.append([2,-1])
solutions.append(2)

tests.append([1,2,3])
solutions.append(6)

tests.append([-10,9,20,None,None,15,7])
solutions.append(42)

for i in range(len(tests)):
    new_tree = TreeNode()
    new_tree.fromArray(tests[i])
    ans = Solution().maxPathSum(new_tree)
    print('T',i,'R',ans,solutions[i])

