class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t):
            return False

        t_pointer = 0
        for i in range(len(s)):
            
            found_s_i = False
            loop_num = len(t[t_pointer:])
            for j in range(loop_num):
                if s[i] == t[t_pointer]:
                    found_s_i = True
                    t_pointer += 1
                    break
                else:
                    t_pointer += 1
            if found_s_i == False:
                return False
        

        return True
