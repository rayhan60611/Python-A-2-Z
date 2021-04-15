# favLang = {}
# a = input("Enter your favorite language Shubham\n")
# b = input("Enter your favorite language Ankit\n")
# c = input("Enter your favorite language Sonali\n")
# d = input("Enter your favorite language Harshita\n")
# favLang['shubham'] = a
# favLang['ankit'] = b
# favLang['sonali'] = c
# favLang['harshita'] = d

# print(favLang)

List=[]

for item in range(1,3):
    l=input (f"Enter Your name <space> then favourite language: ")
    k=l.split()
    List.append(k)
print(List)
 
di = dict(i for i in List)
print(di)