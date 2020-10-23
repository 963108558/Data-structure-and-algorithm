# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。


class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenth = len(s)
        if lenth < 2:
            return s
        max_lenth = 1
        result = s[0]
        for i in range(lenth - 1):
            odd = self.centerSpread(s,i,i)
            even = self.centerSpread(s,i,i+1)
            max_str = odd if len(odd) > len(even) else even
            if len(max_str) > max_lenth :
                max_lenth = len(max_str)
                result = max_str
        return result

    def centerSpread(self,s: str,left: int,right: int):
        lenth = len(s)
        i = left
        j = right
        while i >= 0 and j < lenth:
            if s[i] == s[j]:
                i -=1
                j +=1
            else:
                break
        return s[i+1:j]
