class Solution:
    def solution(self, s, i, substr):

        if i > len(s) - 1:
            return substr, -1

        if s[i].isdigit(): 
            num = ''
            while s[i].isdigit():
                num += s[i]
                i += 1
         
            string, end_i = self.solution(s, i+ 1, '')

            substr = substr + int(num) * string
            if (end_i + 1) < len(s):

                returned_val = self.solution(s, end_i + 1, '')
                # try:
                #     return substr + returned_val
                # except:
                return substr + returned_val[0], returned_val[1] 
            else:
                return substr, end_i
        elif s[i] == ']':
            return substr, i
        
        else:
            return self.solution(s, i + 1, substr + s[i])

        
    def decodeString(self, s: str) -> str:
        return self.solution(s, 0, '')[0]