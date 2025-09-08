class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        def recursion_isSubsequence(index_s, index_t):

            #base cases
            if index_s == len(s): #finished exploring the source
                return True
            if index_t == len(t): #ran out of the target sequence before finish exploring the source
                return False

            if s[index_s] == t[index_t]: #the character matches!
                #increment both
                index_s += 1
                index_t += 1 
                return recursion_isSubsequence(index_s, index_t)
            else:
                #increment only t's index. 
                index_t += 1   
                return recursion_isSubsequence(index_s, index_t)
            
            # index_t += 1 をif文の外に出すよりもこの書き方の方が私には分かりやすいです..! 
            #条件に当てはまらない場合にはsを増やさないことが綺麗に見えるので。
        
        return recursion_isSubsequence(0, 0) #start with index 0 for both sequences.
