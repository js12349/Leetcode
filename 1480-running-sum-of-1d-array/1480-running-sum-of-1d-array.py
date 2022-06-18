class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [nums[0]]
        
        for n in nums[1:]:
            ret.append(ret[-1] + n)
        return ret