q= int(input("Press a calculating method you want to use:1 for (+),2 for (-),3 for (*), 4 for(/):"))


if  q == 1:
    z= int(input("Enter your 1st Number:"))
    x= int(input("Enter your 1st Number:"))

    sum = z + x
    print("The sum is:", sum)


elif q == 2:

    z= int(input("Enter your 1st Number:"))
    x= int(input("Enter your 1st Number:"))

    sum = z - x
    print("The difference is:", sum)

elif q == 3:

    z= int(input("Enter your 1st Number:"))
    x= int(input("Enter your 1st Number:"))

    sum = z * x
    print("The product is:", sum)


elif q == 4:

    z= int(input("Enter your 1st Number:"))
    x= int(input("Enter your 1st Number:"))

    sum = z / x
    print("The quotient is:", sum)

else:
    print("Invalid Input")
