class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True

        hashmap = {}
        for i in range(len(t)):
            letter = t[i]
            if letter in hashmap:
                hashmap[letter].append(i) #the list is already sorted because we append one by one from the start of the target to the end
            else:
                hashmap[letter] = [i]

        positions = []
        for i in range(len(s)):
            letter = s[i]
            if letter not in hashmap: #if the letter doesn't exist in the target, there is no chance that source is a subsequence
                return False
            else:
                positions.append(hashmap[letter])
        
        #at this point, it is confirmed that all source letters are included in target letters.
        previous_position = min(hashmap[s[0]]) #not sure how many elements exists in this list, so just get min.
        for i in range(1, len(s)):
            letter = s[i]
            letter_positions = hashmap[letter] #list

            flag_larger_exists = False
            for p in letter_positions:
                if p > previous_position: 
                    previous_position = p
                    flag_larger_exists = True
                    break
            if flag_larger_exists == False:
                return False
        
        return True

