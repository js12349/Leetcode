# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1->2->3
        # currNode = 1
        # nextNode = 2, 3
        # currNode.next = 1.next = None
        # currNode = nextNode = 2,3
        # prevNode = 1
        # ----
        # 
        
        prevNode = None
        currNode = head
        
        while currNode != None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        
        return prevNode