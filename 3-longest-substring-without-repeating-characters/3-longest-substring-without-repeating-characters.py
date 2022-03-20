class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        lst = [0]
        for start in range(len(s)):
            sub = s[start]
            for end in s[(start+1):]:
                if end not in sub:
                    sub += end
                else:
                    break
            lst.append(len(sub))
        return max(lst)