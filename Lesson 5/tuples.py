#Tuples elements cannot be changed once they've been declared
#declare a tuple
my_tuple = ("Hello",1,2,"World",3,4)
print(my_tuple)

#declare new tuple
my_tuple = ("a",2,"c",4,"e",6,"g",8,"i",9,"j",10)
print(my_tuple[0])  #print the first element
print(my_tuple[:])  #print all the elements

#declare new tuple
my_tuple = ("p","r","o","g","r","a","m","m","i","n","g")
print(len(my_tuple))        #number of elements contained in the tuple
print(my_tuple.count("m"))  #number of times m occurs in the tupple

#declare new tuple
my_tuple = ("John","James","Kim","Joseph")
for name in my_tuple:
    print("Hello ", name)
    
