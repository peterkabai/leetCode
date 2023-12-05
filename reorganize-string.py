# https://leetcode.com/problems/reorganize-string/submissions/
class Solution:
    def reorganizeString(self, s: str) -> str:
        m, ret = {}, " "
        for c in s:
            if c not in m: m[c] = 1
            else: m[c] += 1

        for i in range(len(s)):
            a = sorted(m.items(), key=lambda x:x[1], reverse=True)
            nextLetter = a[0][0]
            if ret[-1] is not nextLetter:
                ret += nextLetter
                m[nextLetter] -= 1
                if m[nextLetter] == 0: del m[nextLetter]
            else:
                if len(a) == 1:
                    return ""
                nextLetter = a[1][0]
                ret += nextLetter
                m[nextLetter] -= 1
                if m[nextLetter] == 0: del m[nextLetter]
        return ret.strip(" ")
        