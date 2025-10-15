# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max1 = 0
        for i in range(len(s)):
            l,r = i,i
            #print(a,b)
            while l >=0 and r < n and s[l]==s[r]:
                if max1 < r-l+1:
                    max1= r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
            #even
            l=i
            r=i+1
            while l >=0 and r < n and s[l]==s[r]:
                if max1 < r-l+1:
                    max1= r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res