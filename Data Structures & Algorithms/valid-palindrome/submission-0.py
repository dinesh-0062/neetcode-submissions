class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip characters that are not letters or digits.
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare case-insensitively.
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
