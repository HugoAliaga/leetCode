class Solution:
    def lengthOfLastWord2(self, s: str) -> int:
        if not s:
            return 0
        res = ''
        lastWord = ''
        for i in s:
            if i == ' ' and len(res)>0:
                lastWord = res
                res = ''
            elif i != ' ':
                res += i
        if res: return len(res)

        return len(lastWord)

    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        word_list = s.split(' ')
        while '' in word_list:
            word_list.remove('')

        return len(word_list[-1])

tests= []
solutions = []

tests.append("Hello World")
solutions.append(5)

tests.append("   fly me   to   the moon  ")
solutions.append(4)

tests.append("luffy is still joyboy")
solutions.append(6)

for i in range(len(tests)):
    ans = Solution().lengthOfLastWord(tests[i])
    print('T',i,'R',ans,solutions[i])