def flatten(lst):
    result = []
    for sublist in lst:
        for item in sublist:
            result.append(item)

    return result
print(flatten([[1, 2], [3, 4]]))
