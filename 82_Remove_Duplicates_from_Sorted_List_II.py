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
    def deleteDuplicates2(self, head):
        if not head: return None
        if not head.next: return head
        if head.next.val == head.val:
            fast = head
            while True:
                if fast and fast.val == head.val:
                    fast = fast.next
                else:
                    head = fast
                    if fast: fast = fast.next
                    if not fast or fast.val != head.val:
                        break
        if head and head.next:
            pre = head
            while pre and pre.next:
                slow= pre.next
                if slow.next:
                    fast = slow.next
                    if slow.val == fast.val:
                        while True:
                            if slow and fast and slow.val == fast.val:
                                fast = fast.next
                            else:
                                slow = fast
                                if fast: fast = fast.next
                                if not fast or fast.val != slow.val:
                                    break
                pre.next = slow
                pre = pre.next

        if head: return head.toArray()
        else: return []

    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        dummy = pre = ListNode(0)
        dummy.next = head
        while pre and pre.next:
            slow= pre.next
            if slow.next:
                fast = slow.next
                if slow.val == fast.val:
                    while True:
                        if slow and fast and slow.val == fast.val:
                            fast = fast.next
                        else:
                            slow = fast
                            if fast: fast = fast.next
                            if not fast or fast.val != slow.val:
                                break
            pre.next = slow
            pre = pre.next

        if not dummy.next: return []
        return dummy.next.toArray()

tests = []
solutions = []

tests.append([1])
solutions.append([1])

tests.append([1,2,3,4,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,8,8,8,9,10,11,12,13,14,14,14])
solutions.append([1,2,3,4,9,10,11,12,13])

tests.append([1])
solutions.append([1])

tests.append([1,1,1,1,1,1,1,2])
solutions.append([2])

tests.append([1,1,1,1,1,1,1,2,2,2,2,2])
solutions.append([])

tests.append([1,2,3,3,4,4,5])
solutions.append([1,2,5])

tests.append([1,1,1,2,3])
solutions.append([2,3])

for i in range(len(tests)):
    elem = ListNode()
    elem.fromArray(tests[i])
    ans = Solution().deleteDuplicates(elem)
    print('T',i,'R',ans,solutions[i])