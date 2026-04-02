class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s:
            if i.isalnum():
                ans = ans + i.lower()
        return ans == ans[::-1]


s = Solution()
print(s.isPalindrome(s="A man, a plan, a canal: Panama"))
