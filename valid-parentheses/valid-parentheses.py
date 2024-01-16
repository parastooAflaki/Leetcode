class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        
        open_bracks = ['(', '[', '{']
        close_bracks = [')', ']', '}']
        
        bracks_dict = {}
        for char1, char2 in zip(open_bracks, close_bracks):
            bracks_dict[char1] = char2
            bracks_dict[char2] = None
        for char in s:
            if char not in open_bracks + close_bracks:
                continue
            if char_stack and bracks_dict[char_stack[-1]] == char:
                char_stack = char_stack[:-1]
            else:
                char_stack = char_stack + [char]
            
            # print(char_stack)
        if len(char_stack) == 0:
            return True
        return False