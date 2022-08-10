def numDuplicates(name, price, weight):
    # Write your code here
    # every list has same iteration
    duplicates = 0
    duplicates_arr = []
    index_already_compared_against = []
    
    for i in range(0, len(name)):
        if i in index_already_compared_against:
            continue
        for j in range(0, len(name)):
            if j != i:
                if name[j] == name[i]:
                    if price[j] == price[i]:
                        if weight[j] == weight[i]:
                            if i not in duplicates_arr:
                                duplicates_arr.append(i)
                                index_already_compared_against.append(i)
                            if j not in duplicates_arr:
                                duplicates_arr.append(j)
                                index_already_compared_against.append(j)
                            print(f"within loop {duplicates_arr}")
        if len(duplicates_arr) > 0:
            # remove first index/index being compared to
            temp = len(duplicates_arr) - 1
            duplicates += temp
            duplicates_arr = []
    print(duplicates)

name = ["ball", "box", "ball", "ball", "box"]
price = [2, 2, 2, 2, 2]
weight = [1, 2, 1, 1, 2]
numDuplicates(name, price, weight)