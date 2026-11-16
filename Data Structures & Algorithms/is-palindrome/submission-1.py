class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            # push start pointer
            while not s[start].isalnum() and start < end:
                start += 1

            # push end pointer 
            while not s[end].isalnum() and start < end:
                end -= 1

            if not s[start].lower() == s[end].lower():
                return False

            start += 1
            end -= 1

        return True