def add_dots(add):
    return '.'.join(add)
a = add_dots('test')
print(a)

def remove_dots(remove):
    return remove.replace(".","")
b = remove_dots(a)
print(b)
