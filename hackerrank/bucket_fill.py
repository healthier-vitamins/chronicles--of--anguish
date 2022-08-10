picture = ["aabba", "aabba", "aaacb"]



def strokesRequired(picture):
    # Write your code here
    letters = ['a', 'b', 'c']
    p = 0
    strokes = 0
    attempt = []
    for i in picture:
        attempt.append(list(i))
    hit = 0
            
    while p != len(letters):
        for i, word in enumerate(picture):
            for j, letter in enumerate(word):
                if j != len(word) - 1:
                    if word[j + 1] == letter and letters[p] == letter:
                        attempt[i][j] = 1
                        attempt[i][j + 1] = 1
                else:
                    if letter == word[len(word) - 1]:
                        attempt[i][j] = 1
        print(f"before: {attempt}")
        for j in range(len(picture[0])):
            for i, word in enumerate(picture):
                if i != len(picture) - 1:
                    if picture[i][j] == picture[i + 1][j] and picture[i][j] == letters[p]:
                        attempt[i][j] = 1
                        attempt[i + 1][j] = 1
                else:
                    # test i with max case
                    if picture[i][j] == picture[len(picture) - 1][j] and picture[i][j] == letters[p]:
                        attempt[i][j] = 1
        strokes += 1
        print(attempt)
        incomplete = False
        for i in range(len(attempt)):
            if letters[p] in attempt[i]:
                incomplete = True
                break
        if incomplete == False:
            p += 1
    return(strokes)
print(strokesRequired(picture))

