import re 
class Solution() : 
    def isPalindrome(self, s:str) -> bool: 

        string = re.sub("^a-zA-Z0-9", "", s)  #uses memory to create new string 

        rev_index = len(string) - 1 

        for i in range(string) : 
            if i == rev_index : break 
            if string[i].lower != string[rev_index].lower() :  return False 
            rev_index -= 1 

        return True 
    
#testing 

sol = Solution() 
print()


