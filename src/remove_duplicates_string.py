'''
You are given a string s consisting of lowercase English letters. 
A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. 
It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
and this is the only possible move.  
The result of this move is that the string is "aaca", 
of which only "aa" is possible, so the final string is "ca".

Example 2:

Input: s = "azxxzy"
Output: "ay"




'''

# Version récursive (divide & conquer)
# Complexité temps : O(n log n), espace : O(log n) pour la pile d'appels + copies de chaînes
def remove_duplicates_rec(s: str) -> str:
    if len(s) == 1:
        return s  # O(1)
    
    if len(s) == 2:
        return "" if s[0] == s[1] else s  # O(1)
    
    mid = len(s) // 2
    # On divise la chaîne en deux parties : récursion sur chaque moitié
    left = remove_duplicates_rec(s[:mid])  # O(n/2 log n/2)
    right = remove_duplicates_rec(s[mid:]) # O(n/2 log n/2)
    
    # Gestion des doublons à la frontière : dans le pire des cas, O(n)
    while left and right and left[-1] == right[0]:
        left = left[:-1]   # O(k) pour copier la sous-chaîne (k ≤ n)
        right = right[1:]  # O(k) pour copier la sous-chaîne

    # Concaténation : O(len(left) + len(right)) = O(n)
    return left + right


# Version itérative avec pile (stack)
# Complexité temps : O(n), espace : O(n)
def remove_duplicate_it(s: str) -> str:
    stack = []  # O(1)
    for char in s:  # boucle sur chaque caractère → O(n)
        if stack and stack[-1] == char:  # comparaison sommet de pile → O(1)
            stack.pop()  # suppression paire → O(1)
        else:
            stack.append(char)  # ajout dans la pile → O(1)
    return "".join(stack)  # reconstitution de la chaîne → O(n)






print(remove_duplicates_rec("azxxzy"))