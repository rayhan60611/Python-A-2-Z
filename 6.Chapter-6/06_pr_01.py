
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")





#By using list

l=[]
for x in range(1,5):
    y=input(f"Enter Your {x} Number: ")
    l.append(int(y))


l.sort(reverse=True)
print(f"Your Gratest Number Is: {l[0]}")