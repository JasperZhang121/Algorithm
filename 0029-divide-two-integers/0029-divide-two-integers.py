class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        doubles = []
        powersOfTwo = []

        # Nothing too exciting here, we're just making a list of doubles of 1 and
        # the divisor. This is pretty much the same as Approach 2, except we're
        # actually storing the values this time. */
        powerOfTwo = 1
        while divisor >= dividend:
            doubles.append(divisor)
            powersOfTwo.append(powerOfTwo)
            # Prevent needless overflows from occurring...
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor # Double divisor
            powerOfTwo += powerOfTwo

        # Go from largest double to smallest, checking if the current double fits.
        # into the remainder of the dividend.
        quotient = 0
        for i in reversed(range(len(doubles))):
            if doubles[i] >= dividend:
                # If it does fit, add the current powerOfTwo to the quotient.
                quotient += powersOfTwo[i]
                # Update dividend to take into account the bit we've now removed.
                dividend -= doubles[i]

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return quotient if negatives != 1 else -quotient