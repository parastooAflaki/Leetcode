class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found = False
        MAX_NUM = 100 + 1
        for end in range(len(nums) - 1, 0 - 1, -1):
            if found:
                break
            cur_num = nums[end]
            min_index = None
            min_value = MAX_NUM
            for i in range(end + 1, len(nums)):
                if nums[i] > cur_num and nums[i] < min_value:
                    min_value = nums[i]
                    min_index = i
            
            if min_index != None:
                nums[min_index] = cur_num
                nums[end] = min_value
                nums[end+1:] = sorted(nums[end+1:])
                found = True
        
        if not found:
            nums[:] = sorted(nums[:])
            
         