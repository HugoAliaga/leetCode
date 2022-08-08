from math import ceil


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def fromArray(self,array):
        if array:
            self.val = array[0]
            array_div = array[1:]
            if array_div:
                if array_div[0] == None:
                    self.left = TreeNode()
                    self.left.fromArray([None])
                    self.right = TreeNode()
                    self.right.fromArray(array_div[1:])
                elif len(array_div)>1 and array_div[1]==None:
                    self.left = TreeNode()
                    self.left.fromArray(array_div[:1]+array_div[2:])
                    self.right = TreeNode()
                    self.right.fromArray([None])
                else:
                    ln = ceil(len(array_div)/2)
                
                    array_left = array_div[:ln]
                    array_right = array_div[ln:]

                    if array_left:
                        self.left = TreeNode()
                        self.left.fromArray(array_left)
                    if array_right:
                        self.right = TreeNode()
                        self.right.fromArray(array_right)

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
            if self.val:
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
    def isValidBST(self, node) -> bool:
        def dfs(node,thisMin,thisMax):
            if not node or not node.val: return True
            if node.val:
                if node.val >= thisMax or node.val <= thisMin: return False

                ans1 = dfs(node.left,thisMin,min(thisMax,node.val))

                ans2 = dfs(node.right,max(thisMin,node.val),thisMax)
            return ans1 and ans2

        return dfs(node,-float('inf'),float('inf'))

tests = []
solutions = []

tests.append([5,4,6,None,None,3,7])
solutions.append(False)

tests.append([2,2,2])
solutions.append(False)

tests.append([1,1])
solutions.append(False)

tests.append([2,1,3])
solutions.append(True)

tests.append([5,1,4,None,None,3,6])
solutions.append(False)

for i in range(len(tests)):
    val = TreeNode()
    val.fromArray(tests[i])
    ans = Solution().isValidBST(val)
    print('T',i,'R',ans,solutions[i])