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
    def isBalanced(self, root) -> bool:
        
        def dfs(node,idx):
            if not node: return idx
            left = dfs(node.left,idx+1)
            right = dfs(node.right,idx+1)
            if not left or not right or abs(left-right)>1: return False

            return max(left,right)

        return dfs(root,0) != False
tests = []
solutions = []

tests.append([3,9,20,None,None,15,7])
solutions.append(True)


tests.append([1,2,2,3,3,None,None,4,4])
solutions.append(False)

tests.append([])
solutions.append(True)



for i in range(len(tests)):
    tree1 = TreeNode()
    tree1.fromArray(tests[i])
    ans = Solution().isBalanced(tree1)
    print('T',i,'R',ans,solutions[i])