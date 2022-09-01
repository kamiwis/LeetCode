class Solution:
    def romanToInt(self, s: str) -> int:
        number_dict = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD':400, 'CM': 900}
        roman = s
        integer = 0
        while len(roman) > 0:
            if roman[0:2] in number_dict:
                integer += number_dict[roman[0:2]]
                roman = roman.replace(roman[0:2], "", 1)
            else:
                integer += number_dict[roman[0]]
                roman = roman.replace(roman[0], "", 1)
        return integer
                
                
        