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

        # In the first loop, we simply find the largest double of divisor
        # that fits into the dividend.
        # The >= is because we're working in negatives. In essence, that
        # piece of code is checking that we're still nearer to 0 than we
        # are to INT_MIN.
        highest_double = divisor
        highest_power_of_two = -1
        while highest_double >= HALF_MIN_INT and dividend <= highest_double + highest_double:
            highest_power_of_two += highest_power_of_two
            highest_double += highest_double

        # In the second loop, we work out which powers of two fit in, by
        # halving highest_double and highest_power_of_two repeatedly.
        # We can do this using bit shifting so that we don't break the
        # rules of the question :-)
        quotient = 0
        while dividend <= divisor:
            if dividend <= highest_double:
                quotient += highest_power_of_two
                dividend -= highest_double
            # We know that these are always even, so no need to worry about the
            # annoying "bit-shift-odd-negative-number" case.
            highest_power_of_two >>= 1
            highest_double >>= 1

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return quotient if negatives == 1 else -quotient