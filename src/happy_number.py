'''

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1

Example 2:

Input: n = 2
Output: false


1 = 1
2 = 4 =  
 

'''

def digits_squared(n : int) -> int:
    if n < 10 :
        return n * n
    
    m = n % 10
    
    return m * m + digits_squared(n // 10)
    

def happy_number(n : int) -> bool:
    
    if n in [2, 3, 4, 5, 6] :
        return False 
    
    elif n == 1 :
        return True
    
    return happy_number(digits_squared(n))
    
    
print(happy_number(145))
    
    