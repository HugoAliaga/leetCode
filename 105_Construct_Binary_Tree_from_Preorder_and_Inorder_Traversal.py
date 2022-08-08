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
    def buildTree(self, preorder,indorder) -> bool:

        def dfs(pre,ino):
            if not pre:
                return None
            root = TreeNode(pre[0])
            pos_ino = ino.index(pre[0])
            ino_left = ino[0:pos_ino]
            ino_right = ino[pos_ino+1:]

            pre_left = pre[1:len(ino_left)+1]
            pre_right = pre[len(ino_left)+1:]

            root.left = dfs(pre_left,ino_left)
            root.right = dfs(pre_right,ino_right)
            return root
        return dfs(preorder,indorder)
tests = []
solutions = []

tests.append([[1,2],[1,2]])
solutions.append([1,2])


tests.append([[3,9,20,15,7],[9,3,15,20,7]])
solutions.append([3,9,20,None,None,15,7])

tests.append([[1],[1]])
solutions.append([1])

for i in range(len(tests)):
    ans = Solution().buildTree(tests[i][0],tests[i][1])
    print('T',i,'R',ans.toArray(),solutions[i])