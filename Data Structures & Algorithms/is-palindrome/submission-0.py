class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_clean = "".join(ch for ch in s if ch.isalnum())
        length = len(s_clean)
        i = 0
        j = length - 1

        while i <= j:  
            if not s_clean[i] == s_clean[j]:
                return False
            i += 1
            j -= 1
                
        return True
        