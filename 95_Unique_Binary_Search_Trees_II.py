from functools import lru_cache
from math import ceil, floor

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
    def generateTrees(self,n):

        versions = []
        @lru_cache(maxsize=None)
        def dfs(options,path):
            if options =='':
                versions.append(path)
            for i in range(len(options)):
                dfs(options[:i]+options[i+1:],path+options[i])

        options = ''.join([str(el) for el in range(1,n+1)])
        for i in range(len(options)):
            dfs(options[:i]+options[i+1:],options[i])
        ans = []
        ans_to_array = []
        for i in versions:
            new_tree = TreeNode()
            for j in i:
                new_tree.insert(int(j))
            
            if new_tree.toArray() not in ans_to_array:
                ans.append(new_tree)
                ans_to_array.append(new_tree.toArray())
        return ans
tests = []
solutions = []

tests.append(3)
solutions.append([[1,None,2,None,3],[1,None,3,2],[2,1,3],[3,1,None,None,2],[3,2,None,1]])

tests.append(1)
solutions.append([1])

for i in range(len(tests)):
    ans = Solution().generateTrees(tests[i])
    for j in ans:
        print(j.toArray())
    print('T',i,ans,solutions[i])