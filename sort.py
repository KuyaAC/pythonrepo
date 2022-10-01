lst = []

n = int(input("Enter a number of Elements:"))

for i in range(0,n):

    ele = int(input())

    lst.append(ele)

    if ele == n:
        break
    
print("The unsorted input are:", lst)

sort = sorted(lst)
print("The sorted lst are:", sort)



