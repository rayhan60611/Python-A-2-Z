#num = int(input("Enter the number: ")) not solved yet
for i in range(3):
    if i==0 or i==2 :
        print("*" * (1),end="")
        print(" " * (1),end="")
        print("*" * (1),end="")
        print(" " * (1),end="")
        print("*" * (1))
    if i==1:
        print("*" * (i),end="")
        print(" " * (i+2),end="")
        print("*" * (i))