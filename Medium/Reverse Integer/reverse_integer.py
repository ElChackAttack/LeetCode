class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sol = str(x)[1::]
            sol = sol[::-1]
            sol = -int(sol)
        else:
            sol = int(str(x)[::-1])
        if (-2**31 < sol < 2**31 - 1):
            return sol
        return 0
