#Problem No 1:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

number =input("Enter Your Number: ")

for i in range(1,11):
    print(f"{number}x{i} = {int(number)*i}")



#Problem No 2:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

l= ['Rayhan','Sumon','Sony','Tony','Sunny']
for name in l:
    if name.startswith("S"):
        print(f"Hello Mr. {name} !!")


#Problem No 3:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

number =input("Enter Your Number: ")
i=1
while i<11:
    print(f"{number}x{i} = {int(number)*i}")
    i+=1


#Problem No 4:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")


#Problem No 5:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

num = int(input("Enter the number: "))
i=1
sum=0
k=1
while i <= num:
    i+=1
    sum+=k
    k+=1
print(f"Sum of N Natural Number is: {sum}")


#Problem No 6:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

num = int(input("Enter the number: "))
j=num+1
fact=1
for i in range(1,j):
    fact=fact*i
print(f"The Factorial value of {num} is : {fact}" )


#Problem No 7:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
num = int(input("Enter the number: "))
for i in range(num):
    print(" " * (num-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (num-i-1),)

#Problem No 8:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

num = int(input("Enter the number: "))
for i in range(num):
    print("*" * (i+1))

#Problem No 9:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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
    

#Problem No 10:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

number =input("Enter Your Number: ")
i=10
while i>0:
    print(f"{number}x{i} = {int(number)*i}")
    i-=1
