from ast import List


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i]=nums2[i]
        return nums1.sort()

    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1: return not nums2
        if not nums2: return nums1
        stack = [float('inf')]
        nums2+=[float('inf')]*m
        idx=0
        for i in range(m):
            minNum = min(nums1[i],nums2[idx],stack[-1])
            if minNum == nums1[i]:
                continue
            elif minNum == stack[-1]:
                temp = nums1[i]
                nums1[i]=stack.pop(1)
                stack.insert(1,temp)
            else:
                stack.insert(1,nums1[i])
                nums1[i]=nums2[idx]
                idx+=1
        for i in range(m,m+n):
            minNum = min(nums2[idx],stack[-1])
            if minNum == nums2[idx]:
                nums1[i]=nums2[idx]
                idx+=1
            else :
                nums1[i]=stack.pop()
        return nums1

tests = []
solutions = []

tests.append([[-1,0,1,1,0,0,0,0,0],4,[-1,0,2,2,3],5])
solutions.append([-1,-1,0,0,1,1,2,2,3])

tests.append([[4,5,6,0,0,0],3,[1,2,3],3])
solutions.append([1,2,3,4,5,6])
tests.append([[2,0],1,[1],1])
solutions.append([1,2])
tests.append([[1,2,3,0,0,0],3,[2,5,6],3])
solutions.append([1,2,2,3,5,6])

tests.append([[1],1,[],0])
solutions.append([1])

tests.append([[0],  0, [1], 1])
solutions.append([1])

for i in range(len(tests)):
    ans = Solution().merge(tests[i][0],tests[i][1],tests[i][2],tests[i][3])
    print('T',i,'R',ans,solutions[i])
