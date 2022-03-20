class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(set(s)) == len(s):
            return len(s)
        
        substr = ""
        substr_set = set()
        maxlen = 0
        for char in s:
            if char not in substr_set:
                substr += char
                substr_set.add(char)
                maxlen = max(maxlen, len(substr))
            else:
                substr = substr.split(char)[1] + char
                substr_set = set(list(substr))
        return maxlen