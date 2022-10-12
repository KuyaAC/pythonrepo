result = []
lst = [[1,2], [3,4]]

for flatten in lst:
    for item in flatten:
        result.append(item)
        
print(result)
