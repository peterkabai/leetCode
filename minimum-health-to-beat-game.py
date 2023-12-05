# https://leetcode.com/problems/minimum-health-to-beat-game/description/
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        total, m = sum(damage) + 1, max(damage)
        if m > armor: return total - armor
        else: return total - m