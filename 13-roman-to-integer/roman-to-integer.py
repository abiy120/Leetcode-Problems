class Solution:
    def romanToInt(self, r: str) -> int:
        res = 0
        rmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i, c in enumerate(r):
            if i == len(r) - 1:
                res += rmap[c]
            else:
                if rmap[c] >= rmap[r[i+1]]:
                    res += rmap[c]
                else:
                    res -= rmap[c]
        return res
