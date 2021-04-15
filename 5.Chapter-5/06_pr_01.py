myDict = {
    "Pakha": "Fan",
    "Dabba": "Box",
    "bostu": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Key Word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))