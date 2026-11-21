class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        
        if len(nums) >= 3:
           
            for i in range(len(nums)-2):
                if i> 0 and nums[i-1] == nums[i]:
                    continue
                left_num = i+1
                right_num = len(nums)-1
                while left_num < right_num :
                    find_num = nums[i] +  nums[left_num] +  nums[right_num]
                    if find_num == 0:
                        ans.append([nums[i] , nums[left_num], nums[right_num]])
                        right_num -= 1
                        left_num += 1
                        while (
                            left_num < right_num
                            and nums[left_num] == nums[left_num - 1]
                        ):
                            left_num += 1
                        while (
                            left_num < right_num
                            and nums[right_num] == nums[right_num + 1]
                        ):
                            right_num -= 1
                    elif find_num > 0:
                        right_num -= 1
                    elif find_num < 0:
                        left_num += 1
        return ans