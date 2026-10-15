class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_text = "".join(sorted(s))
        t_text = "".join(sorted(t))
        if s_text==t_text:
            return True
        else:
            return False

        