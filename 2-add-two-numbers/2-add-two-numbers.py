# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = int(self.convertListToNum(l1))
        num2 = int(self.convertListToNum(l2))
        sum = str(num1 + num2)
        
        return self.createLLFromNum(self.reverseStr(sum))
        
    
    def convertListToNum(self, ll):
        if ll.next == None:
            return str(ll.val)
        else:
            return self.convertListToNum(ll.next) + str(ll.val)
        
    def createLLFromNum(self, num):
        if num == '':
            return None
        else:
            return ListNode(num[0], self.createLLFromNum(num[1:]))
        
    def reverseStr(self, strnum):
        rev = ''
        
        idx = len(strnum)-1
        while idx > -1:
            rev += strnum[idx]
            idx -= 1
        return rev