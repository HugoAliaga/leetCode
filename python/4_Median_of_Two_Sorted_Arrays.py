from ntpath import join


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        """
        joinedList = nums1+nums2
        joinedList.sort()
        if len(joinedList)%2 == 0:
            suma = 0.5*joinedList[int(len(joinedList)/2-1)] + 0.5*joinedList[int(len(joinedList)/2)]
            return suma

        else:
            return joinedList[int(len(joinedList)/2-0.5)]


tests = []
results = []

tests.append([[1,3],[2,4]])
results.append(2.5)

tests.append([[1],[2,4]])
results.append(2)

tests.append([[1,3],[2]])
results.append(2)

for i in range(len(tests)):
    result = Solution().findMedianSortedArrays(tests[i][0],tests[i][1])
    print('This is test '+str(i),result,results[i])