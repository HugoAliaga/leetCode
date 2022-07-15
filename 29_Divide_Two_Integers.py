class Solution(object):
    def sign_function(self,x):
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return -1

    def divide(self, dividend, divisor):
        if divisor == 0 :
            return None

        result = 0
        negative = False
        signDividend = self.sign_function(dividend)
        signDivisor = self.sign_function(divisor)
        if signDividend != signDivisor:
            negative=True
        dividend=str(abs(dividend))
        divisor=abs(divisor)

        resto = 0
        cociente = 0
        while dividend:
            resto+=int(dividend[0])
            dividend = dividend[1:]
            while resto >= divisor:
                resto-=divisor
                cociente+=1
            if dividend:
                resto = int(str(resto)+'0')
                cociente = int(str(cociente)+'0')

        if negative:
            cociente = -cociente
        if cociente > 2**31-1:
            cociente = 2**31-1
        if cociente < -2**31:
            cociente = -2**31
        return cociente
tests= []
solutions=[]

tests.append([10,2])
solutions.append(5)

tests.append([10,3])
solutions.append(3)

tests.append([7,-3])
solutions.append(-2)
print(10<<=1)
tests.append([-2147483648,-1])
solutions.append(-2147483648)

for i in range(len(tests)):
    result=Solution().divide(tests[i][0],tests[i][1])
    print('Test ' + str(i),'Result',result,solutions[i])