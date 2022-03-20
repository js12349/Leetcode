class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(set(s)) == len(s):
            return len(s)
        
        substr = ""
        maxlen = 0
        for char in s:
            if char not in substr:
                substr += char
                maxlen = max(maxlen, len(substr))
                #print(maxlen)
            else:
                substr = substr.split(char)[1] + char
        
        return maxlen