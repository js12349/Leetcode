class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        left = 0
        right = sum(nums)
        
        #if left == right:
        #    return -1
        
        for n in range(0, len(nums)):
            if n != 0:
                left += nums[n-1]
            right -= nums[n]
            
            if left == right:
                return n
            
        return -1