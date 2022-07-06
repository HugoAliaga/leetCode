print("Starting")

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxLetters = 0
        letters = ''
        for letter in s:
            if letter in letters:
                indexLetter = letters.index(letter)
                letters = letters[indexLetter+1:]+letter

            else :
                letters += letter
                if len(letters)>maxLetters:
                    maxLetters = len(letters)

        return maxLetters
        

tests = []
solutions = []

tests.append('abcabcbb')
solutions.append(3)

tests.append('bbbbb')
solutions.append(1)

tests.append('pwwkew')
solutions.append(3)

for i in range(len(tests)):
    solution = Solution().lengthOfLongestSubstring(tests[i])
    print('Test' + str(i),solution,solutions[i])