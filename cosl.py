def double_letters(u):
    for i in u:
        if i*2 in u:
            return True
    return False
print('Test a consecutive Character')
string = input("Enter a string:")
str =  string
print(double_letters(str))
