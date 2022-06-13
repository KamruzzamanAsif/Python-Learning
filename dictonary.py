my_dictonary = {
    "Asif" : 1217,
    "Sharif" : 1211
}

print(my_dictonary)
# print using loop
for x in my_dictonary:
    print(x, end=" ",)
    print(my_dictonary[x])

# key print
for x in my_dictonary.keys():
    print(x)

# value print
for x in my_dictonary.values():
    print(x)

# access items
x = my_dictonary["Asif"]
print(x)

# add new element
my_dictonary["fahad"] = 1204

print(my_dictonary)

# remove item
my_dictonary.pop("Asif")
print(my_dictonary)

del my_dictonary["fahad"]
print(my_dictonary)
