# https://leetcode.com/problems/reorder-data-in-log-files/submissions/
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        d, l = [], []
        for lo in logs:
            if lo.split(" ")[1].isdigit(): d.append(lo)
            else: l.append(lo)
        l = sorted(l, key=lambda x: (" ".join(x.split(" ")[1:]), x.split(" ")[0]))
        return l + d