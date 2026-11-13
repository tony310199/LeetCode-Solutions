class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # 如果目前的子區間已經是完全遞增排序，直接取最左邊元素即可
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break

            m = (l + r) // 2
            ans = min(ans, nums[m])

            # 判斷 m 屬於左半段還是右半段
            if nums[m] >= nums[l]:
                # m 在左半段，最小值必在 m 的右邊
                l = m + 1
            else:
                # m 在右半段，最小值必在 m 的左邊
                r = m - 1

        return ans