class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if not n:
            return None
        if int(n) == 1:
            return '1'
        else:
            counter = 1
            ans = str(1)
            while counter < n:
                newAns = []
                pre = None
                count = 0
                for el in ans:
                    if el != pre:
                        newAns.append(str(count))
                        newAns.append(pre)
                        count=1
                        pre = el
                    else:
                        count +=1
                newAns.append(str(count))
                newAns.append(pre)
                newAns.pop(0)
                newAns.pop(0)
                ans = ''.join(newAns)
                counter+=1
                    
            return ans

tests = []
solutions = []

tests.append(1)
solutions.append(1)

tests.append(2)
solutions.append(11)

tests.append(3)
solutions.append(21)

tests.append(4)
solutions.append(1211)

tests.append(5)
solutions.append(111221)

for i in range(len(tests)):
    result = Solution().countAndSay(tests[i])
    print('T ' + str(i),'R',result,solutions[i])