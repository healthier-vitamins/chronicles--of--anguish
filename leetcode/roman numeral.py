class Solution:
    s = ""
    characters = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    def __init__(self):
        self.s = input("Input: s = ")
        while(True):
            if len(self.s) <= 1 or len(self.s) >= 15:
                print("Not less than 1 or more than 15")
                self.s = input("Input: s = ")
            characters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
            count = 0
            for letter in self.s:
                for character in characters:
                    if letter.upper() == character:
                        count += 1
            if count != len(self.s):
                print("Only 'I', 'V', 'X', 'L', 'C', 'D', 'M' allowed.")
                self.s = input("Input: s = ")
            else:
                break

    def romanToInt(self) -> int:
        characters_used = {}
        for input_index, input_letter in enumerate(self.s):
            for letter, value in self.characters.items():
                if input_letter.upper() == letter:
                    characters_used[letter] = characters_used.get(letter, 0) + 1
                    """
                    characters_used[letter] = characters_used[letter] + 1
                    .push letter and .push count in 2 separate arrays
                    since they're the same index, able pump it into a dictionary
                    """
        return characters_used

test = Solution()
print(test.romanToInt())

# https://leetcode.com/problems/roman-to-integer/