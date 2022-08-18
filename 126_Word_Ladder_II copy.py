from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:

        # 1. Create adjacency list
        def adjacencyList():

            # Initialize the adjacency list
            adj = defaultdict(list)

            # Iterate through all words
            for word in wordList:

                # Iterate through all characters in a word
                for i, _ in enumerate(word):

                    # Create the pattern
                    pattern = word[:i] + "*" + word[i + 1 :]

                    # Add a word into the adjacency list based on its pattern
                    adj[pattern].append(word)

            return adj

        # 2. Create reversed adjacency list
        def bfs(adj):

            # Initialize the reversed adjacency list
            reversedAdj = defaultdict(list)

            # Initialize the queue
            queue = deque([beginWord])

            # Initialize a set to keep track of used words at previous level
            visited = set([beginWord])

            while queue:

                # Initialize a set to keep track of used words at the current level
                visitedCurrentLevel = set()

                # Get the number of words at this level
                n = len(queue)

                # Iterate through all words
                for _ in range(n):

                    # Pop a word from the front of the queue
                    word = queue.popleft()

                    # Generate pattern based on the current word
                    for i, _ in enumerate(word):

                        pattern = word[:i] + "*" + word[i + 1 :]

                        # Itereate through all next words
                        for nextWord in adj[pattern]:

                            # If the next word hasn't been used in previous levels
                            if nextWord not in visited:

                                # Add such word to the reversed adjacency list
                                reversedAdj[nextWord].append(word)

                                # If the next word hasn't been used in the current level
                                if nextWord not in visitedCurrentLevel:

                                    # Add such word to the queue
                                    queue.append(nextWord)

                                    # Mark such word as visited
                                    visitedCurrentLevel.add(nextWord)

                # Once we done with a level, add all words visited at this level to the visited set
                visited.update(visitedCurrentLevel)

                # If we visited the endWord, end the search
                if endWord in visited:
                    break

            return reversedAdj

        # 3. Construct paths based on the reversed adjacency list using DFS
        def dfs(reversedAdj, res, path):
            if path[0] == beginWord:            # If the first word in a path is beginWord, we have succesfully constructed a path
                res.append(list(path))          # Add such path to the result
            word = path[0]                      # Else, get the first word in a path
            for nextWord in reversedAdj[word]:  # Find next words using the reversed adjacency list
                path.appendleft(nextWord)       # Add such next word to the path
                dfs(reversedAdj, res, path)     # Recursively go to the next word
                path.popleft()                  # Remove such next word from the path

            # Return the result
            return res

        # Do all three steps
        adj = adjacencyList()
        reversedAdj = bfs(adj)
        res = dfs(reversedAdj, [], deque([endWord]))

        return res



tests = []
solutions = []

tests.append(["hot","dog",["hot","dog"]])
solutions.append([])

tests.append(["hot","dog",["hot","dog","dot"]])
solutions.append([["hot","dog","dot"]])

tests.append(["hit","cog",["hot","dot","dog","lot","log","cog"]])
solutions.append( [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]])

tests.append(["hit","cog",["hot","dot","dog","lot","log"]])
solutions.append( [])

for i in range(len(tests)):
    ans = Solution().findLadders(tests[i][0],tests[i][1],tests[i][2])
    print('T',i,'R',ans,solutions[i])