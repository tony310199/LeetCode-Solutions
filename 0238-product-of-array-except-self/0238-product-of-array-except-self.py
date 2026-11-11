class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        pre = 1 
        #prefix product
        for i in range(len(nums)):
            if i == 0:
                ans.append(1)
            else:
                ans.append(pre)
            pre *= nums[i]
        #suffix product
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suffix = 1
            else:
                ans[i] *= suffix
            suffix *= nums[i]
        
        return ans