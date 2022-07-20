class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num_1 = []
        num_2 = []
        for i in num1:
            num_1.append(int(i))
        for i in num2:
            num_2.append(int(i))

        total = 0
        for i in range(len(num_1)-1,-1,-1):
            for j in range(len(num_2)-1,-1,-1):
                total += num_1[i]*num_2[j]*(10**(len(num_1)-1-i+len(num_2)-1-j))
        return total

tests = []
solutions = []

tests.append(['12','20'])
solutions.append(str(12*20))

tests.append(['234','423'])
solutions.append(str(234*423))

tests.append(['34','0'])
solutions.append(str(34*0))


for i in range(len(tests)):
    result = Solution().multiply(tests[i][0],tests[i][1])
    print('T',i,'R',result,solutions[i])