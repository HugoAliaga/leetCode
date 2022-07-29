from ntpath import join
import re


class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path: return '/'
        new_path = path.split('/')

        i = len(new_path)-1
        to_delete = 0
        while new_path and i >=0:
            if new_path[i]=='':
                del new_path[i]
            elif new_path[i]=='..':
                del new_path[i]
                to_delete+=1
            elif new_path[i]=='.':
                del new_path[i]
            elif to_delete>0:
                    del new_path[i]
                    to_delete -=1
            i-=1
        new_path='/'.join(new_path)
        new_path='/'+new_path

        #new_path = re.sub('([\/])([a-zA-Z0-9]*)([\/\.\.\/])','/',new_path)
        return new_path

tests= []
solutions = []

tests.append("/a/./b/../../c/")
solutions.append('/c')

tests.append("/home/")
solutions.append("/home")

tests.append('/../')
solutions.append('/')

tests.append("/home//foo/")
solutions.append("/home/foo")

for i in range(len(tests)):
    ans = Solution().simplifyPath(tests[i])
    print('T',i,'R',ans,solutions[i])