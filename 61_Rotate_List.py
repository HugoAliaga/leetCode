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
    def rotateRight(self, head, k):

        if not head: return None
        if k == 0: return head
        fast = head
        slow = head
        n=0
        while n<k:
            if not fast:
                return self.rotateRight(head,k%n)
            fast = fast.next
            n+=1
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        if not fast:
            return head
        next = slow.next
        slow.next= None
        fast.next= head
        return next

tests = []
solutions = []

tests.append([[1,2,3,4,5],2])
solutions.append([4,5,1,2,3])

tests.append([[1,2,3,4,5],15])
solutions.append([1,2,3,4,5])

tests.append([[0,1,2],4])
solutions.append([2,0,1])

tests.append([[1,2],1])
solutions.append([2,1])

tests.append([[1,2],2])
solutions.append([1,2])

tests.append([[1],1])
solutions.append([1])

tests.append([[1,2,3],2000000000])
solutions.append([3,2,1])

for i in range(len(tests)):
    val = ListNode()
    val.fromArray(tests[i][0])
    ans = Solution().rotateRight(val,tests[i][1])
    print('T',i,'R',ans.toArray(),solutions[i])
