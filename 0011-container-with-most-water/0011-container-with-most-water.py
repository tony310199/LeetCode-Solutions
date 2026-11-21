class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_n = 0
        right_n = len(height)-1
        max_ans = 0
        while left_n<right_n:
            curr_ans = min(height[left_n],height[right_n]) * (right_n-left_n)
            if curr_ans>max_ans:
                max_ans = curr_ans
            if height[left_n] >= height[right_n]:
                right_n -= 1
            else:
                left_n += 1

        return max_ans