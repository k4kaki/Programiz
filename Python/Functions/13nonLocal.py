x=0
def main_fun():
    x=20
    def local_fun():
        global x
        x=25
        print("Inside local",x)
    local_fun()
    print("Inside main",x)
main_fun()
print("Outside main:",x)
