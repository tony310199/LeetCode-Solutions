class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num_h = nums[0]  # 記錄歷史出現過的最大乘積
        min_num = nums[0]    # 記錄「以當前數字結尾」的最小乘積
        max_num = nums[0]    # 記錄「以當前數字結尾」的最大乘積

        for i in range(1, len(nums)):
            # 1. 算出以 nums[i] 結尾的新最大、最小乘積
            curr_max = max(nums[i], nums[i] * max_num, nums[i] * min_num)
            curr_min = min(nums[i], nums[i] * max_num, nums[i] * min_num)
            
            # 2. 直接更新狀態給下一輪使用（保持連續性）
            max_num = curr_max
            min_num = curr_min

            # 3. 更新全域歷史最大值
            max_num_h = max(max_num, max_num_h)

        return max_num_h

        