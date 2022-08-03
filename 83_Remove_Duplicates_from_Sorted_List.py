from ast import Or


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
    def deleteDuplicates(self, head):
        if not head: return head
        pre = fast = head
        while fast:
            if fast.val == pre.val:
                fast = fast.next
            else:
                pre.next = fast
                pre = pre.next
                if fast.next:
                    fast=fast.next
        pre.next = fast
        return head

tests = []
solutions = []

tests.append([1])
solutions.append([1])

tests.append([1,2,3,4,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,8,8,8,9,10,11,12,13,14,14,14])
solutions.append([1,2,3,4,5,6,7,8,9,10,11,12,13,14])

tests.append([1])
solutions.append([1])

tests.append([1,1,1,1,1,1,1,2])
solutions.append([1,2])

tests.append([1,1,1,1,1,1,1,2,2,2,2,2])
solutions.append([1,2])

tests.append([1,2,3,3,4,4,5])
solutions.append([1,2,3,45])

tests.append([1,1,1,2,3])
solutions.append([1,2,3])

for i in range(len(tests)):
    elem = ListNode()
    elem.fromArray(tests[i])
    ans = Solution().deleteDuplicates(elem)
    print('T',i,'R',ans.toArray(),solutions[i])