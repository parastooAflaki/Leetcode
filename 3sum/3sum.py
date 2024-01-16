class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        results = []
        for i in range(len(nums) - 2):
            two_sum = 0 - nums[i]
            start = i + 1 # first next number
            end = len(nums) - 1 # last number
          
            while end - start >= 1:
               
                if nums[start] + nums[end] == two_sum:
                    results.append((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] > two_sum:
                    end -= 1
                else:
                    start += 1
                
                
        return set(results)
            
        