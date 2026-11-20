class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left_num = 0
        right_num = len(nums)-1
        ans = -1
        if len(nums)>1:
            while  left_num != right_num:
                mid_num = (left_num + right_num) // 2
                #確認哪邊有序
                if nums[left_num] <= nums[mid_num]  :
                    if nums[left_num] <= target <= nums[mid_num] :
                        right_num = mid_num
                    else:
                        left_num = mid_num + 1
                elif nums[mid_num]  <= nums[right_num]  :
                    if nums[mid_num] <= target <= nums[right_num] :
                        left_num = mid_num + 1
                    else:
                        right_num = mid_num
                    

                if nums[left_num] == target:
                    ans = left_num
                    break
                elif nums[right_num] == target:
                    ans = right_num
                    break
                elif nums[mid_num] == target:
                    ans = mid_num
                    break
        elif len(nums)== 1 and target == nums[0]:
            ans = 0
        return ans

            
