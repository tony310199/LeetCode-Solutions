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

            max_current = max(nums[i],nums[i]*max_curr,nums[i]*min_curr)
            min_current = min(nums[i],nums[i]*max_curr,nums[i]*min_curr)
            max_curr = max_current
            min_curr = min_current
            if max_curr>max_h:
                max_h = max_curr

        return max_h