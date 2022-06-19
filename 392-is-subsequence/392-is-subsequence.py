class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_array = list(s)
        
        for tchar in t:
            if len(s_array) > 0:
                if tchar == s_array[0]:
                    s_array.pop(0)
            else:
                break
                
        return len(s_array) == 0