class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = 0
        for num in nums:
            idx2 = idx + 1
            for num2 in nums[idx2:]:
                if (num + num2) == target:
                    return [idx,idx2]
                idx2 += 1
            idx += 1