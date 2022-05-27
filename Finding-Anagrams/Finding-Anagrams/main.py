# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

s1 = "listen"
s2 = "silent"

def check(s1, s2):
    if(sorted(s1) == sorted(s2)):
        # print("these strings are anagrams")
        return True
    else:
        # print("these srings are ot anagrams")
        return False
        
print (check(s1, s2))
   
    # [assignment] Add your code here

    

