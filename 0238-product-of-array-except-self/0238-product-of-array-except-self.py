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
            ans.append(pre)
            pre *= nums[i]
        #suffix product
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans