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
    def sumNumbers(self, root) -> int:
        def dfs(node):
            if not node.left and not node.right:
                return [str(node.val)]
            ans = []
            if node.left:
                left = dfs(node.left)
                for i in left:
                    ans.append(str(node.val) + i)
            if node.right:
                right = dfs(node.right)
                for i in right:
                    ans.append(str(node.val) + i)
            return ans
        numbers = dfs(root)
        ans = 0
        for i in numbers:
            ans+=int(i)
        return ans


tests = []
solutions = []

tests.append([1,2,3])
solutions.append(25)

tests.append([4,9,0,5,1])
solutions.append(1026)

for i in range(len(tests)):
    tree_el = TreeNode()
    tree_el.fromArray(tests[i])
    ans = Solution().sumNumbers(tree_el)
    print('T',i,'R',ans,solutions[i])