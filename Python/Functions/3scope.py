def scope():
    x=10
    return x
x=20
print("Inside",scope())
print("Outside",x)
print("Inside",scope())
