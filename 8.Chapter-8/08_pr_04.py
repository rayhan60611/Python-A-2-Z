# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

n=int(input("Enter a Number: "))
sum = 0
def sumOfNnumber(n):
    if n == 1:
        return 1
    return n + sumOfNnumber(n-1)
    
n=sumOfNnumber(n)
print(f"sum is : {n}")