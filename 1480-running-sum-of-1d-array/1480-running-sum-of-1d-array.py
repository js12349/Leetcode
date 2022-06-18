class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [nums[0]]
        
        for n in range(1, len(nums)):
            ret.append(ret[-1] + nums[n])
        return ret