
def isPalindrome(string: str) -> bool:
    
    start, end = 0, len(string) - 1
    
    while start <= end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False
         
    return True

def isPalindromeRec(string: str) -> bool:
    
    if len(string) == 1:
        return True
    
    elif len(string) == 2:
        return string[0] == string[1]
    
    return string[0] == string[-1] and isPalindromeRec(string[1: len(string) - 1])

print(isPalindromeRec("racecar"))