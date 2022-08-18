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
    def sortedArrayToBST(self, nums) -> bool:
        ln = len(nums)
        def dfs(arr):
            if not arr: return None
            mid = int(len(arr)/2)
            root = TreeNode(arr[mid])
            root.left = dfs(arr[:mid])
            root.right = dfs(arr[mid+1:])
            return root

        
        return dfs(nums)
tests = []
solutions = []

tests.append([-10,-3,0,5,9])
solutions.append([0,-3,9,-10,None,5])


tests.append([1,3])
solutions.append([1,None,3] )

tests.append([1,2,3,4,5,6,7,8,9,10,11,12])
solutions.append([7,4,10,2,6,9,12,1,3,5,None,8,None,11])


tests.append([1,2,3,4,5,6,7,8,9,10,11])
solutions.append([6,3,9,2,5,8,11,1,None,4,None,7,None,10])



for i in range(len(tests)):
    ans = Solution().sortedArrayToBST(tests[i])
    print('T',i,'R',ans.toArray(),solutions[i])