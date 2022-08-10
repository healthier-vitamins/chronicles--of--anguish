picture = ["aabba", "aabba", "aaacb"]

def strokesRequired(picture):
    no_of_fill = 0
    letters = ["a", "b" ,"c"]

    # populate is_filled array based on picture's 2d array
    is_filled = []
    for i in range(len(picture)):
        col = []
        for j in range(len(picture[i])):
            col.append(0)
        is_filled.append(col)

    p = 0
    while p != len(letters) - 1:
        for i, h in enumerate(picture):
            for j, w in enumerate(h):
                max_length = len(h)
                if j + 1 != max_length:
                    if h[j + 1] == h[j] and w == letters[p]:
                        is_filled[i][j] = 1
                        is_filled[i][j + 1] = 1
                else:
                    if h[j] == h[max_length - 1] and w == letters[p]:
                        is_filled[i][max_length - 1] = 1
                        is_filled[i][j] = 1
        # swap j and i
        for j in range(0, len(picture[0])):
            for i, h in enumerate(picture):
                if i + 1 != len(picture):
                    if picture[i + 1][j] == picture[i][j] and picture[i][j] == letters[p]:
                        is_filled[i][j] = 1
                        is_filled[i + 1][j] = 1
                else:
                    if picture[i][j] == picture[len(picture) - 1][j] and picture[i][j] == letters[p]:
                        is_filled[i][j] = 1
                        is_filled[len(picture) - 1][j] = 1
        p += 1
        no_of_fill += 1
    return is_filled, no_of_fill
print(strokesRequired(picture))

