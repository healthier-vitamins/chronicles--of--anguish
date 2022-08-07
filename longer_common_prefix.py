class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            for j in range(len(strs[1:])):
                if i >= len(strs[j]):
                    return result
                elif strs[0][i] != strs[j][i]:
                    return result
                
            result = result + strs[0][i]


# https://leetcode.com/problems/longest-common-prefix/