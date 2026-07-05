class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        mx = 0

        for x in gain:
            alt += x
            mx = max(mx, alt)

        return mx