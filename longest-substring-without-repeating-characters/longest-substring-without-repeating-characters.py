class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N_ASCI_CHARS = 128 + 1
        last_visited_indexes = [-1] * N_ASCI_CHARS # indexes in list correspond to the asci code of the character
        
        max_length = 0
        start = 0
        for end in range(0, len(s)):
            asci_code = ord(s[end])
            last_visited_index = last_visited_indexes[asci_code]

            if last_visited_index != -1 and last_visited_index >= start:
                start = last_visited_index + 1 # next character in the string after the repeated char
                    
            last_visited_indexes[asci_code] = end
            cur_length = end - start + 1            
            max_length = max(max_length, cur_length)
        return max_length
                