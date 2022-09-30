lst = []

n = int(input("Enter number of Elements:"))


for i in range(0,n):
    ele = int(input())
    
    lst.append(ele)
    
    if ele == n:
        break 
print(lst)

even_list = filter(lambda x: x%2 == 0,lst)
final= sum(even_list)
print("Sum of the even in array:", final)


