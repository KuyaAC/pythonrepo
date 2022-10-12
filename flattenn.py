result = []
flatten = [[1,2], [3,4]]
result = [item for sublist in flatten for item in sublist]
print(result)
