# Definition for singly-linked list.
from statistics import LinearRegression


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
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        ans  = ListNode()
        head = ans
        list1=list1.next
        list2=list2.next

        while list1 or list2:
            ans.next=ListNode()
            ans=ans.next
            if list1:
                if list2:
                    if list1.val<list2.val:
                        ans.val=list1.val
                        list1=list1.next
                    else:
                        ans.val=list2.val
                        list2=list2.next
                else:
                    ans.val=list1.val
                    list1=list1.next
            else:
                ans.val = list2.val
                list2=list2.next

        return head

    def mergeTwoLists2(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        ans  = ListNode()
        head = ans

        while list1 and list2:
            ans.next=ListNode()
            ans=ans.next

            if list1.val<list2.val:
                ans.val=list1.val
                list1=list1.next
            else:
                ans.val=list2.val
                list2=list2.next
        ans.next = list1 or list2
        return head.next.next        

tests = []
solutions = []

tests.append([[],[]])
solutions.append([])

tests.append([[1,2,4],[1,3,4]])
solutions.append([1,1,2,3,4,4])

for i in range(len(tests)):
    list1 = ListNode()
    list2 = ListNode()
    list1.fromArray(tests[i][0])
    list2.fromArray(tests[i][1])
    result = Solution().mergeTwoLists2(list1,list2)
    print('Test ' + str(i),'Result',result.toArray(),solutions[i])
        