class Solution(object):
    def longestCommonPrefix(self, strs):

        strMinor = len(strs[0])

        for str in strs:
            if len(str) < strMinor:
                strMinor = len(str)

        commomPrefix = ""

        for i in range(0, strMinor):
            for str in strs:
                if strs[0][i] != str[i]:
                    return commomPrefix
            commomPrefix += strs[0][i]

        return commomPrefix   
