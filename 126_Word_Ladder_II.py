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

    def findLadders(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList: return 0
        option_dict = self.create_dict(beginWord,wordList)
        ln = len(beginWord)
        visited = set()
        queue = deque()
        answers = [[beginWord]]
        ans = []
        queue.appendleft([beginWord,1])
        visited.add(beginWord)
        while queue:
            next_word, level = queue.popleft()
            for i in range(ln):
                temp_word = next_word[:i]+'.'+next_word[i+1:]
                for word in option_dict[temp_word]:
                    if word not in visited:
                        visited.add(word)
                        queue.append([word,level+1])
                        for group in answers:
                            if group[-1]==next_word:
                                answers.append(group+[word])

        for group in answers:
            if group[-1]==endWord:
                ans.append(group)
        return ans



tests = []
solutions = []

""" tests.append(["hot","dog",["hot","dog"]])
solutions.append([])

tests.append(["hot","dog",["hot","dog","dot"]])
solutions.append([["hot","dog","dot"]]) """

tests.append(["hit","cog",["hot","dot","dog","lot","log","cog"]])
solutions.append( [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]])

tests.append(["hit","cog",["hot","dot","dog","lot","log"]])
solutions.append( [])

for i in range(len(tests)):
    ans = Solution().findLadders(tests[i][0],tests[i][1],tests[i][2])
    print('T',i,'R',ans,solutions[i])