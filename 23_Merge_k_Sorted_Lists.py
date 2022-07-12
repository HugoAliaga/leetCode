import datetime
import heapq as h

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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ans = ListNode()
        for i in range(len(lists)):
            lists[i] = lists[i].next

        remainingNumbers = True
        while remainingNumbers:
            value = float("inf")
            
            list = None
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val<value:
                        value = lists[i].val
                        list = i
            if type(list)==int:
                ans.next = ListNode()
                ans = ans.next
                lists[list]=lists[list].next
                ans.val = value
                
            else: 
                remainingNumbers = False
        return head
    def mergeTwoLists(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head = ans = ListNode()
        while l1 and l2:
            ans.next = ListNode()
            ans = ans.next
            if l1.val < l2.val:
                ans.val = l1.val
                l1=l1.next
            else:
                ans.val = l2.val
                l2=l2.next
        ans.next = l1 or l2
        return head.next

    def mergeKLists2(self,lists):
        if len(lists)==0:
            return None
        while True:
            if len(lists)==1:
                return lists[0]
            l1,l2 = lists.pop(), lists.pop()
            merged = self.mergeTwoLists(l1,l2)
            lists.append(merged)
    def mergeKListsHeap(self,lists):
        heap = []
        if len(lists)==0:
            return None
        for i in range(len(lists)):
            if lists[i]:
                h.heappush(heap,(lists[i].val,i))
                lists[i]=lists[i].next
        
        head = ans = ListNode()
        while heap:
            ans.next = ListNode()
            ans = ans.next
            ans.val,i = h.heappop(heap)
            if lists[i]:
                h.heappush(heap,(lists[i].val,i))
                lists[i]=lists[i].next
        return head.next


tests = []
solutions = []      

tests.append([[1,4,5],[1,3,4]])
solutions.append([1,1,3,4,4,5])

tests.append([[1,4,5],[1,3,4],[2,6]])
solutions.append([1,1,2,3,4,4,5,6])


for i in range(len(tests)):
    newArray = []
    for j in range(len(tests[i])):
        listN = ListNode()
        listN.fromArray(tests[i][j])
        newArray.append(listN)
    
    result = Solution().mergeKListsHeap(newArray)
        
    print('Test ' + str(i),'Result',result.toArray(),solutions[i])
