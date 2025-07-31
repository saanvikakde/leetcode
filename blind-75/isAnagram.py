class Solution: 
    def isAnagram(self, s:str, t:str) -> bool: 
        
        if len(s) != len(t) : return False 
       
        word_s = dict() 
        word_t = dict() 

        for i in range(len(s)) : #can't do for each since traversing two words at once 

            word_t[t[i]] = word_t.get(t[i], 0) + 1 #t[i] is letter_t 
            word_s[s[i]] = word_s.get(s[i], 0) + 1 #s[i] is letter_s 
        
        return word_t == word_s 

#testing 

sol = Solution() 
print(sol.isAnagram("cat", "tac"))
print(sol.isAnagram("cat", "bra"))





