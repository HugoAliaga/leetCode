class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def toArray(self):
        globalAns = []
        visited = [self]
        def dfs(node):
            if not node: return None
            ans = []
            for el in node.neighbors:
                ans.append(el.val)
            globalAns.append(ans)
            for el in node.neighbors:
                    if el not in visited:
                        visited.append(el)
                        dfs(el)
        dfs(self)
        return globalAns
    def fromArray(self,array):
        self.val = 1
        node_dict = {}
        node_dict[1]=self
        for i in range(1,len(array)):
            newNode = Node(i+1)
            node_dict[i+1]=newNode
        for i in range(len(array)):
            for j in array[i]:
                node_dict[i+1].neighbors.append(node_dict[j])


class Solution:
    def cloneGraph(self, node):
        if not node: return None
        node_dict_new = {}
        def dfs(node):
            if not node: return None
            if node.val in node_dict_new: return node_dict_new[node.val]
            myNode = Node()
            myNode.val = node.val
            node_dict_new[node.val] = myNode
            for el in node.neighbors:
                myNode.neighbors.append(dfs(el))
            return myNode
        return dfs(node)


tests = []
solutions = []

tests.append([[2,4],[1,3],[2,4],[1,3]])
solutions.append([[2,4],[1,3],[2,4],[1,3]])

for i in range(len(tests)):
    thisNode = Node()
    thisNode.fromArray(tests[i])
    ans = Solution().cloneGraph(thisNode)
    print('T',i,'R',ans.toArray(),solutions[i])