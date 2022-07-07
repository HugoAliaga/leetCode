class Solution(object):
    def longestPalindrome(self, s):
        lenS=len(s)
        if lenS <= 1: return s
        
        longestAnswer=''
        letter=0
        while letter <lenS:
            counter = 1
            res = s[letter]
            while counter<=letter and counter+letter<lenS and s[letter-counter]==s[letter+counter]:
                res = s[letter-counter:letter+counter+1]
                counter +=1

            if len(res)>len(longestAnswer):
                longestAnswer = res



            res = ''
            newWordEven = s[letter:letter+2]
            if newWordEven[0]==newWordEven[-1]:
                res = newWordEven
                counter = 1
                while counter<=letter and counter+letter<lenS-1 and s[letter-counter]==s[letter+counter+1]:
                    res = s[letter-counter:letter+counter+2]
                    counter +=1

            if len(res)>len(longestAnswer):
                longestAnswer = res

            letter+=1

        return longestAnswer
        




tests = []
results = []

tests.append('adda')
results.append('adda')

tests.append('ababd')
results.append('aba')

tests.append('ccc')
results.append('ccc')

tests.append('cbbd')
results.append('bb')

for i in range(len(tests)):
    result = Solution().longestPalindrome(tests[i])
    print('Test ' + str(i),'Result',result,results[i])