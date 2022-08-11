input_arr = [ 'k', 'w', 'a', 'd', 'x', 'a','i' ]
vowels = ['a', 'e', 'i', 'o', 'u']

def count_vowels (input_arr):
    count = 0
    for i in range(len(input_arr)):
        for index in range(len(vowels)):
            if input_arr[i] == vowels[index]:
                count += 1
                continue
    return count
print(count_vowels(input_arr))