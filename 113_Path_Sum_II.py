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
    def hasPathSum(self, root,targetSum) -> bool:
        
        def dfs(node,path):
            if not node or node.val == None: return False
            if path + node.val == targetSum and not node.left and not node.right: return True
            left = dfs(node.left,path+node.val)
            right = dfs(node.right,path+node.val)
            return left or right
        return dfs(root,0)
tests = []
solutions = []

tests.append([[0,1,1],1])
solutions.append(True)

tests.append([[-2,None,-3],-5])
solutions.append(True)

tests.append([[5,4,8,11,None,13,4,7,2,None,None,None,1],22])
solutions.append(True)

tests.append([[1,2,3],5])
solutions.append(False)

tests.append([[],0])
solutions.append(False)



for i in range(len(tests)):
    tree1 = TreeNode()
    tree1.fromArray(tests[i][0])
    ans = Solution().hasPathSum(tree1,tests[i][1])
    print('T',i,'R',ans,solutions[i])