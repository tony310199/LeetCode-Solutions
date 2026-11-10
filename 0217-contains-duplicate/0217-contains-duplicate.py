class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = {nums[0] : 1}
        for i in range(1,len(nums)):
            if temp.get(nums[i]) != None:
                return True
            temp[nums[i]] = 1
        return False