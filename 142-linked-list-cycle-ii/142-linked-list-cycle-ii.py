# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        pointer = head
        
        while pointer != None:
            if pointer in seen:
                return pointer
            else:
                seen.add(pointer)
                pointer = pointer.next
        
        return None