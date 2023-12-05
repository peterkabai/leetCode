# https://leetcode.com/problems/group-anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m, groups = {}, []
        for s in strs:
            b = "".join(sorted([*s]))
            if b in m.keys(): m[b].append(s)
            else: m[b] = [s]
        for group in m.keys(): groups.append(m[group])
        return(groups)