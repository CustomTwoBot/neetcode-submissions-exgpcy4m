class Solution:
    def isHappy(self, n: int) -> bool:
        seenVals = set()

        while n not in seenVals:
            seenVals.add(n)

            total = 0
            while n > 0:
                digit = n % 10
                total += pow(digit, 2)
                n //= 10
            n = total
            if total == 1:
                return True
        return False