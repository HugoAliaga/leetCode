from collections import defaultdict
from collections import deque
class Solution:
    def create_dict(self,beginWord,wordList):
        ln = len(beginWord)
        wordList.append(beginWord)
        prev_dict = defaultdict(list)
        for word in wordList:
            prev_dict[word]=[]
            for i in range(ln):
                prev_dict[word[:i] + "." + word[i+1:]].append(word) 
        """         option_dict = {}
        for word in wordList:
            option_dict[word]=[]
            for i in range(ln):
                for el in prev_dict:
                    if el != word:
                        intermed_word = el[:i]+'.'+el[i+1:] 
                        if intermed_word in prev_dict[word] and el not in option_dict[word]:
                            option_dict[word].append(el) """
        return prev_dict

    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList: return 0
        option_dict = self.create_dict(beginWord,wordList)
        ln = len(beginWord)
        visited = set()
        queue = deque()
        ans = []
        queue.appendleft([beginWord,1])
        visited.add(beginWord)
        while queue:
            next_word, level = queue.popleft()
            for i in range(ln):
                temp_word = next_word[:i]+'.'+next_word[i+1:]
                for word in option_dict[temp_word]:
                    if word not in visited:
                        if word == endWord:
                            return level+1
                        visited.add(word)
                        queue.append([word,level+1])
        return 0

tests = []
solutions = []

tests.append(["hot","dog",["hot","dog"]])
solutions.append(0)

tests.append(["hot","dog",["hot","dog","dot"]])
solutions.append(3)

tests.append(["hit","cog",["hot","dot","dog","lot","cog"]])
solutions.append(5)


for i in range(len(tests)):
    ans = Solution().ladderLength(tests[i][0],tests[i][1],tests[i][2])
    print('T',i,'R',ans,solutions[i])