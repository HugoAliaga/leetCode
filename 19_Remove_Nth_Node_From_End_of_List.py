# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def fromArray(self,array):
        head = self
        for el in array:
            self.next = ListNode(el)
            self=self.next
    def toArray(self):
        endArray = []
        self=self.next
        while self:
            endArray.append(self.val)
            self=self.next
        return endArray



class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        moving1 = head
        moving2 = moving1
        moving1=moving1.next
        moving2=moving2.next

        i=0
        while i <n:
            moving2 = moving2.next
            i+=1
        if not moving2:
            return head.next

        while moving2.next:
            moving2=moving2.next
            moving1=moving1.next

        if moving1.next:
            moving1.next=moving1.next.next
        else:
            del moving1.val
        return head

tests = []
solutions = []

tests.append([[1,2,3,4,5],2])
solutions.append([1,2,3,5])

tests.append([[1],1])
solutions.append([])

""" tests.append([[1,2],1])
solutions.append([1])

tests.append([[1,2],2])
solutions.append([2]) """

for i in range(len(tests)):
    test = ListNode()
    test.fromArray(tests[i][0])
    result = Solution().removeNthFromEnd(test,tests[i][1])
    print('Test ' + str(i),'Result',result.toArray(),solutions[i])
        