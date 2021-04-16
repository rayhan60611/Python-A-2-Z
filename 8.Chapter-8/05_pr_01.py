def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(13, 55, 2)
print("The value of the maximum is " + str(m))

# different Solve Problem no 1 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
f1=0
f2=0
def maximum ( x , y , z):
    if x>y:
        f1=x
    else:
        f1=y

    if y>z:
        f2=y
    else:
        f2=z
    if f1>f2:
        return f1
    else:
        return f2

a=maximum(9, 15, 6)
print( f"The Maximum Number Is: {a}")