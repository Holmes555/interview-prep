class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        numerator, denominator = abs(numerator), abs(denominator)
        integer_part = numerator // denominator

        result.append(str(integer_part))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)

        result.append(".")
        remainder_map = {}
        index = 0
        fractional_part = []
        while remainder != 0:
            if remainder in remainder_map:
                fractional_part.insert(remainder_map[remainder], "(")
                fractional_part.append(")")
                break

            remainder_map[remainder] = index
            remainder *= 10
            fractional_digit = remainder // denominator
            fractional_part.append(str(fractional_digit))
            remainder %= denominator
            index += 1

        result.extend(fractional_part)
        return "".join(result)
