class Solution: 
    def hasDuplicate(self, nums) ->bool: 

        hashset = set() 
        
        for n in nums: 
            if n in hashset: return True # n has alr been added before 
            hashset.add(n) 

        return False 
    
#testing 
sol = Solution() 
print(sol.hasDuplicate([1,2,3,4]))
print(sol.hasDuplicate([1,2,3,3]))


