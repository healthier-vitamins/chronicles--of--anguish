class Solution:
    roman_chars = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    def romanToInt(self, s: str) -> int:
        is_concatenated = False
        total_value = 0
        for input_index, input_letter in enumerate(s):
            if is_concatenated == True:
                is_concatenated = False
                continue
            for letter, value in self.roman_chars.items():
                if input_letter.upper() == letter:
                    if input_index + 1 != len(s):
                        if value < self.roman_chars[s[input_index + 1].upper()]:
                            total_value += (self.roman_chars[s[input_index + 1].upper()] - value)
                            is_concatenated = True
                        else:
                            total_value += value
                    else:
                        total_value += value
        return total_value
        

