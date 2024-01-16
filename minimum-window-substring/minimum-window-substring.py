from collections import defaultdict
class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        target_cnt_map = defaultdict(int)
        window_cnt_map = defaultdict(int)
        for char in t:
            target_cnt_map[char] += 1
        
        # print(target_cnt_map)
        start = 0
        end = 0
        unique_chars_found = 0
        min_sub_str = ''
        
        while end != len(s):
            window_cnt_map[s[end]] += 1

            if s[end] in target_cnt_map and window_cnt_map[s[end]] == target_cnt_map[s[end]]:
                unique_chars_found += 1
            
            # print(unique_chars_found, window_cnt_map, target_cnt_map)
            
            while start <= end and unique_chars_found==len(target_cnt_map):
                    # print(start, end, s[start:end+1])
                    char = s[start]
                    if char in target_cnt_map and window_cnt_map[char] - 1 < target_cnt_map[char]: 
                        unique_chars_found -= 1
                    
                    window_cnt_map[char] -= 1
                    start += 1
                    sub_str =  s[start-1:end + 1]
                    if min_sub_str == '' or len(sub_str) < len(min_sub_str):
                            min_sub_str = sub_str
                            
                    # print(min_sub_str, start, end,)

            end += 1
        
        return min_sub_str
                