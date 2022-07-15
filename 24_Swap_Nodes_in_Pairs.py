# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        nodeNext = head.next
        head.next = self.swapPairs(nodeNext.next)
        nodeNext.next = head
        return nodeNext


tests = []
solutions = []

tests.append([1,2,3,4,5])
solutions.append([2,1,4,3,5])

for i in range(len(tests)):
    list = ListNode()
    list.fromArray(tests[i])
    result = Solution().swapPairs(list)
    print('Test ' + str(i),'Result',result.toArray(),solutions[i])