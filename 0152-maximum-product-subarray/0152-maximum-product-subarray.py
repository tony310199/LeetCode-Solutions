class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_h = nums[0]

        max_curr = nums[0]
        min_curr = nums[0]

        for i in range(1,len(nums)):

            max_c = max(nums[i],nums[i]*min_curr,nums[i]*max_curr)
            min_c = min(nums[i],nums[i]*min_curr,nums[i]*max_curr)
            max_curr = max_c
            min_curr = min_c

            if max_curr>max_h:
                max_h = max_curr
        return max_h
