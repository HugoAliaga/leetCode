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
    def buildTree(self, inorder,postorder) -> bool:

        def dfs(ino,pos):
            if not pos:
                return None
            root = TreeNode(pos.pop())
            pos_ino = ino.index(root.val)
            ino_left = ino[:pos_ino]
            ino_right = ino[pos_ino+1:]

            pos_left = pos[:len(ino_left)]
            pos_right = pos[len(ino_left):]

            root.left = dfs(ino_left,pos_left)
            root.right = dfs(ino_right,pos_right)
            return root
        return dfs(inorder,postorder)
tests = []
solutions = []

tests.append([[9,3,15,20,7],[9,15,7,20,3]])
solutions.append([3,9,20,None,None,15,7])


tests.append([[-1],[-1]])
solutions.append([-1])

tests.append([[1],[1]])
solutions.append([1])

for i in range(len(tests)):
    ans = Solution().buildTree(tests[i][0],tests[i][1])
    print('T',i,'R',ans.toArray(),solutions[i])