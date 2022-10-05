def add_dots(add):
    return '.'.join(add)
i=input("Enter a string:")
a = add_dots(i)
print(a)

def remove_dots(remove):
    return remove.replace(".","")
b = remove_dots(a)
print(b)
