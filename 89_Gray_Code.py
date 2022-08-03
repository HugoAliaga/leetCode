from functools import lru_cache


class Solution:
    def grayCode(self, n):
        ans = [0]*2**n
        def flip(el,position=False):
            ln = len(el)
            if ln <=2:
                if position:
                    return el
                else:
                    return el[::-1]
            else:
                vec1 = el[:int(ln/2)]
                vec2 = el[int(ln/2):]
                if position:
                    vec1 = flip(vec1,True)
                    vec2 = flip(vec2,False)
                    return vec1+vec2
                else:
                    vec1 = flip(vec1,False)
                    vec2 = flip(vec2,True)
                    return vec2+vec1

        def dfs(path,n):
            if n == 0: return [0] + path
            my_numbers = []
            for i in range(2**(n-1),2**n):
                my_numbers += [i]
            my_numbers=flip(my_numbers)

            return dfs(my_numbers + path,n-1)
        return dfs([],n)

tests = []
solutions = []
tests.append(4)
tests.append(3)
solutions.append([0,1,3,2])

tests.append(2)
solutions.append([0,1])

for i in range(len(tests)):
    ans = Solution().grayCode(tests[i])
    print('T',i,'R',ans,solutions[i])
