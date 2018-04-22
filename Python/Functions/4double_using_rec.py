def double_(x):
    if x == 0:
        return 0
    else:
        return double_(x-1)+2
n=int(input("Enter a number to double it:"))
print("Double this",n,"is:::",double_(n))
