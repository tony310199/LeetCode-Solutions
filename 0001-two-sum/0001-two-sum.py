class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic_temp = { nums[0] : 0 }
        for i in range(1,len(nums)):
            obj = target - nums[i]
            
            if dic_temp.get(obj)!= None:
                return i,dic_temp.get(obj)
            dic_temp [nums[i]] = i
        return []