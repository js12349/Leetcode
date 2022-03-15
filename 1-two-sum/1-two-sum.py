class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        idx = 0
        for num in nums:
            idx2 = idx + 1
            for num2 in nums[idx2:]:
                if (num + num2) == target:
                    return [idx,idx2]
                idx2 += 1
            idx += 1
        """
        
        num_index = {}
        for idx, num in enumerate(nums):
            compl = target - num
            if compl in num_index:
                return [idx, num_index[compl]]
            else:
                num_index[num] = idx
        
        """
        for idx, num in enumerate(nums):
            compl = target - num
            rest_nums = nums[(idx+1):]
            if compl in rest_nums:
                return [idx, rest_nums.index(compl) + idx + 1]
        """