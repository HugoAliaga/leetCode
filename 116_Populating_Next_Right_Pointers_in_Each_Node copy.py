class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

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
    def connect(self, root) -> bool:
        if not root or not root.val: return root
        levels = []
        def dfs(root,idx):
            if root == None: return
            if len(levels)<=idx:
                levels.append([])
            levels[idx].append(root)
            dfs(root.left,idx+1)
            dfs(root.right,idx+1)
        dfs(root,0)  
        for i in levels:
            levels[i].append(None)
            for j in range(len(levels[i])-2):
                levels[i][j].next=levels[i][j+1]
        return root
tests = []
solutions = []

tests.append([1,2,3,4,5,6,7])
solutions.append([1,None,2,3,None,4,5,6,7,None])

tests.append([0])
solutions.append([None])

tests.append([])
solutions.append([])

for i in range(len(tests)):
    tree1 = TreeNode()
    tree1.fromArray(tests[i])
    ans = Solution().connect(tree1)
    print('T',i,'R',ans.toArray(),solutions[i])