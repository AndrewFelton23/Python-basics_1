#Sets are unordered and do not contain duplicates

my_set = {1, 2, 3, 4}
print(my_set)

#To add elements
my_set.add(7)
print(my_set)

#Initializing two sets
A = {1, 3, 5, 7, 9, 11}
B = {1, 2, 3, 4, 5}
print("Set A is : ", A)
print("Set B is : ", B)
#The Union prints all elements contained in either sets
print(" The result of A|B is : ", A|B)
#The intersection prints all elements contained in both sets
print("The result of A&B is : ", A&B)
#The difference operator prints the elements not present in both sets
print("The result of A - B is : ", A - B)

