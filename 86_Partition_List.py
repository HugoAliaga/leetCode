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
    def partition(self, head, x: int):
        if not head: return None
        l1 = ListNode(0)
        pre1 = l1
        l2 = ListNode(0)
        pre2=l2
        while head:
            if head.val<x:
                pre1.next=ListNode(head.val)
                pre1=pre1.next
            else:
                pre2.next = ListNode(head.val)
                pre2=pre2.next
            head=head.next


        pre1.next=l2.next
                
        return l1.next

tests = []
solutions = []

tests.append([[1,4,3,2,5,2],3])
solutions.append([1,2,2,4,3,5])

tests.append([[2,1],2])
solutions.append([1,2])

tests.append([[],0])
solutions.append([])

for i in range(len(tests)):
    val = ListNode()
    val.fromArray(tests[i][0])
    ans = Solution().partition(val,tests[i][1])
    print('T',i,'R',ans.toArray(),solutions[i])