x="global"
def global_():
    global x
    x=x*2
    print("inside",x)

global_()
print("outside",x)
