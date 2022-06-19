# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        #[5]
        #[1,2,4]
        if list1 == None and list2 == None:
            return None
        
        if list1 == None and list2 != None:
            return list2
            
        if list1 != None and list2 == None:
            return list1
        
        head = ListNode()
        node = head
        
        while True:
            if list1.val < list2.val:
                node.val = list1.val
                list1 = list1.next
            else:
                node.val = list2.val
                list2 = list2.next
            
            if list1 == None and list2 != None:
                node.next = list2
                break
            if list1 != None and list2 == None:
                node.next = list1
                break
            if list1 == None and list2 == None:
                break
            node.next = ListNode()
            node = node.next
        return head