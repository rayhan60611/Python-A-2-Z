
#Reading from a txt file!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

f = open('sample.txt','r')
data = f.read()
print(data)
f.close()



#Writing to a txt file!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

f = open("write.txt","w")
data = f.write("Now I Am Writting to Rayhan Parvez")
f.close()



#Apending to a txt file!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

f = open("write.txt","a")
data = f.write(" Now I Am Writting to Rafid Arafat")
f.close()