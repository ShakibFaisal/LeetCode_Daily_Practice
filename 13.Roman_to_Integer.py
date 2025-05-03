class Solution :
    def romanToInt(self,s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for ch in reversed(s):  # process from right to left
            value = roman[ch]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total
obj=Solution()
print(obj.romanToInt("MCMXCIV"))

