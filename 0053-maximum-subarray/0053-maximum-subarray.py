class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # kadane's Algorithm
        cur_num = nums[0]
        max_num = nums[0]
        for i in range(1,len(nums)):
            cur_num = max(nums[i],cur_num+nums[i])
            max_num =  max(cur_num,max_num)
        return max_num