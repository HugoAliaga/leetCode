class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s: return not t
        ls = len(s)
        lt = len(t)
        if lt>ls: return ''

        needed_characters = {}
        for char in t:
            if char in needed_characters:
                needed_characters[char]+=1
            else: needed_characters[char]=1
        i,j = 0,0
        i_min, j_min = -1,-1
        min_distance = ls
        while j<ls:
            if s[j] in t:
                needed_characters[s[j]]-=1
                if all(needed_characters[char] <=0  for char in needed_characters):
                    if min_distance > j-i:
                        min_distance = j-i
                        i_min, j_min = i,j
                    condition1 = True
                    while all(needed_characters[char] <=0  for char in needed_characters):
                        if s[i] in t:
                            needed_characters[s[i]]+=1
                        i+=1
                    if min_distance > j-i+1:
                        min_distance = j-i+1
                        i_min, j_min = i-1,j
                    j+=1
                else: j+=1
            else: j+=1
        if i>-1:
            return s[i_min:j_min+1]
        else: return ''

tests = []
solutions = []

tests.append(["ADOBECODEBANC","ABC"])
solutions.append("BANC")

tests.append(["a","a"])
solutions.append("a")

tests.append(["a","aa"])
solutions.append("")

tests.append(["a","b"])
solutions.append("")

for i in range(len(tests)):
    ans = Solution().minWindow(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])