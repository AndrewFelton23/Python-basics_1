#dictionary
#declare a dictionary
my_dictionary = {'Greet' : "Hello", 'name' : "John", 'age' : 24}
print(my_dictionary['Greet'])   #print the element contained at greeting
print(my_dictionary)            #print the entire dictionary
#change the age value
stri = "is this your age " + str(my_dictionary['age']) + " ? "
ans = input(stri)
while ans != "yes":
    try :
        my_dictionary['age'] = int(input("Enter a new age: "))
    except:
        print("Please enter numbers only.")
    else:
        ans = "yes"
for each in my_dictionary:
    print(each, " : ", my_dictionary[each])


