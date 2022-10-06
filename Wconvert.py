w = float(input("Enter your weight:"))
m = input("Enter (k)g or (L)bs:")

if m == 'K'or 'k':
    print("Your weigth in lbs is:", w*2.2)
elif m == 'L'or 'l':
    print("Your weigth in kg is:", w/2.2)
    
