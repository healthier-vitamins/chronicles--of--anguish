from operator import concat


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
        is_concatenated = False
        for input_index, input_letter in enumerate(self.s):
            if is_concatenated == True:
                is_concatenated = False
                continue
            for letter, value in self.characters.items():
                if input_letter.upper() == letter:
                    if input_index + 1 != len(self.s):
                        if value < self.characters[self.s[input_index + 1].upper()]:
                            concatenated_roman = letter + self.s[input_index + 1].upper()
                            updated_value = self.characters[self.s[input_index + 1].upper()] - value
                            characters_used[concatenated_roman] = characters_used.get(concatenated_roman, 0) + updated_value
                            is_concatenated = True
                            continue
                        else:
                            characters_used[letter] = characters_used.get(letter, 0) + value
                    else:
                        characters_used[letter] = characters_used.get(letter, 0) + value
        print(characters_used)

        # for input_index, input_letter in enumerate(self.s):
        #     for letter, value in self.characters.items():
        #         if input_letter.upper() == letter:
        #             # characters_used[letter] = characters_used.get(letter, 0) + 1
        #             if letter not in characters_used:
        #                 characters_used[letter] = 1
        #             else:
        #                 characters_used[letter] += 1
        # total_value = 0
        # for letter, count in characters_used.items():
        #     for letter_fixed, value in self.characters.items():
        #         if letter == letter_fixed:
        #             total_value += value * count

        # print(f"Output: {total_value}")
        # print("Explanation: ", end="")
        # for letter, count in characters_used.items():
        #     print(f"{letter} = {count * self.characters[letter]}, ", end="")
        # print("\n")
        return True

test = Solution()
test.romanToInt()

# https://leetcode.com/problems/roman-to-integer/