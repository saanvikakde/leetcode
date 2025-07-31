from typing import List 

class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        
        differences = dict() #mapping value to index

        for i,n in enumerate(nums) : #traversing nums with counter 
            diff =  target - n #diff is the other value we need 
            if diff in differences : 
                return [i, differences[diff]] #returns current index and that of diff 
            differences[n] = i #stores value to index 
    
#testing 
sol = Solution() 
print(sol.twoSum([3,4,5,6], 7))

