from cgi import test


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def fromArray(self,array):
        self.val = array[0]
        for i in range(1,len(array)):
            self.next = ListNode()
            self=self.next
            self.val = array[i]
    def toArray(self):
        endArray = []
        head = self
        while head:
            endArray.append(head.val)
            head=head.next
        return endArray

class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next= head
        slow = dummy
        
        for i in range(left-1):
            slow=slow.next
        fast = slow
        for i in range(right-left+1):
            fast=fast.next
        if slow and slow.next and fast and fast.next:
            slow.next = self.reverseList(slow.next,right-left,fast.next)
        elif slow and slow.next:
            slow.next = self.reverseList(slow.next,right-left,None)
        return dummy.next
    
    def reverseList(self,head,number,nextLink):
        next = head
        pre = None
        for i in range(number+1):
            nxt = next.next
            next.next=pre
            pre=next
            next=nxt
        head.next = nextLink
        return pre

tests = []
solutions = []

""" tests.append([[1,2,3,4,5],2,4])
solutions.append([1,4,3,2,5])

tests.append([[1,2,3,4,5],2,2])
solutions.append([1,4,3,2,5]) """

tests.append([[3,5],1,2])
solutions.append([5,3])

""" tests.append([[1,2,3,4,5],2,5])
solutions.append([1,4,3,2,5])

tests.append([[5],1,1])
solutions.append([5])

tests.append([[5],0,0])
solutions.append([5]) """


for i in range(len(tests)):
    val = ListNode()
    val.fromArray(tests[i][0])
    #ans = Solution().reverseList(val)
    ans = Solution().reverseBetween(val,tests[i][1],tests[i][2])
    print('T',i,'R',ans.toArray(),solutions[i])
        