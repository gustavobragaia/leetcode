class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        xInverse = x[::-1]

        if x == xInverse:
            return True
        else:
            return False
