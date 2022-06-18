class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        _map_s_to_t = {} #key: s char, value: t char
        _map_t_to_s = {} #key: s char, value: t char
        
        for idx in range(len(s)):
            if s[idx] not in _map_s_to_t:
                _map_s_to_t[s[idx]] = t[idx]
            elif s[idx] in _map_s_to_t and _map_s_to_t[s[idx]] != t[idx]:
                return False
            
            if t[idx] not in _map_t_to_s:
                _map_t_to_s[t[idx]] = s[idx]
            elif t[idx] in _map_t_to_s and _map_t_to_s[t[idx]] != s[idx]:
                return False
        return True
        