class Solution:
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
        s = input("Input: s = ")
        while(True):
            if len(s) <= 1 or len(s) >= 15:
                print("Not less than 1 or more than 15")
                s = input("Input: s = ")

            characters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
            count = 0
            for letter in s:
                for character in characters:
                    if letter.upper() == character:
                        count += 1
            if count != len(s):
                print("Only 'I', 'V', 'X', 'L', 'C', 'D', 'M' allowed.")
                s = input("Input: s = ")

            if len(s) > 1 and len(s) < 15 and count == len(s):
                self.s = s
                break

    def romanToInt(self) -> int:
        romans_used = {}
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
                            romans_used[concatenated_roman] = romans_used.get(concatenated_roman, 0) + updated_value
                            is_concatenated = True
                            continue
                        else:
                            romans_used[letter] = romans_used.get(letter, 0) + value
                    else:
                        romans_used[letter] = romans_used.get(letter, 0) + value
        total_value = 0
        for letter, count in romans_used.items():
            total_value += count

        print(f"Output: {total_value}")
        print("Explanation: ", end="")
        for letter, count in romans_used.items():
            if letter == list(romans_used)[-1]:
                print(f"{letter} = {count}. ", end="")
            else:
                print(f"{letter} = {count}, ", end="")
        print("\n")
        return True

test = Solution()
test.romanToInt()

# https://leetcode.com/problems/roman-to-integer/

