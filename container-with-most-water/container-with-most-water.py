class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = len(height) - 1
        max_amount = 0
        while start != end:
            # print('start', start, 'height[start]', height[start], 'end', end, 'heigh[end]', height[end])
            distance = end - start
            if height[start] <= height[end]:
                cur_amount = height[start] * distance
                start += 1
            else:
                cur_amount = height[end] * distance
                end -= 1
            max_amount = max(cur_amount, max_amount)
            # print(distance, cur_amount)
        return max_amount
        
        