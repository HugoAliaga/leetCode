from typing import List


print('Starting')

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
    def addTwoNumbers(self, l1, l2):
        el1=0
        el2=0
        m=1
        solution = ListNode(0)
        head = solution
        carry =0
        while l1 or l2 or carry:
            sum=0
            if l1:
                sum += l1.val
                l1=l1.next

            if l2:
                sum += l2.val
                l2=l2.next
            if carry:
                sum += carry
                carry=0

            if sum >=10:
                sum = sum-10
                carry =1
            solution.next=ListNode(sum)
            solution=solution.next

        return head.next

tests = []
solutions = []

tests.append([[2,4,3],[5,6,4]])
solutions.append([7,0,8])

tests.append([[9,9,9,9,9,9,9],[9,9,9,9]])
solutions.append([8,9,9,9,0,0,0,1])

for el in range(len(tests)):
    l1=ListNode()
    l2=ListNode()
    l1.fromArray(tests[el][0])
    l2.fromArray(tests[el][1])
    solution = Solution().addTwoNumbers(l1,l2)
    print('Test '+ str(el),solution.toArray(),solutions[el])