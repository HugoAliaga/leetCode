from calendar import c


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

class Solution(object):
    def reverseKGroup(self,head,k):

        if not head:
            return None
        curr = head
        for i in range(k):
            if curr:
                curr = curr.next
            else:
                return head

        prev, curr = None, head
        for i in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        
        head.next = self.reverseKGroup(curr,k)
        
        return prev

    def reverseGroup(self,head):
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


tests = []
solutions = []

tests.append([[1,2],3])
solutions.append([1,2])

tests.append([[1,2,3],3])
solutions.append([3,2,1])

tests.append([[1,2,3,4,5],1])
solutions.append([1,2,3,4,5])

tests.append([[1,2,3,4,5,6,7,8,9],2])
solutions.append([2,1,4,3,6,5,8,7,9])

tests.append([[1,2,3,4,5,6,7,8,9],3])
solutions.append([3,2,1,6,5,4,9,8,7])

for i in range(len(tests)):
    list = ListNode()
    list.fromArray(tests[i][0])
    result = Solution().reverseKGroup(list,tests[i][1])
    print('Test ' + str(i),'Result',result.toArray(),solutions[i])