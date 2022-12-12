#Lists
lista = [1,2,3,4]
#print positions
print('First element: ',lista[0])
print('Second element: ',lista[1])
print('Third element: ',lista[2])
#Find length of list
print(len(lista))
#add a list to another
lista.append(3)
print(lista)
#remove a element
del lista[0]
lista.remove(3)
lista.pop(1)
print(lista)
#Another list with characters as elements
my_list = ["p","e","r","s","o","n","a","l"]
print(my_list)
listlen = len(my_list)
strin = "Enter a number from 0 to " + str(listlen - 1) + " : "
pos = listlen
while pos >listlen -1:
    try:
        pos = int(input(strin))
        print("Value at ", pos, "is : ",my_list[pos])
    except:
        print("Dont enter letters please")
        continue
#printing the values from position 2 to 5
print("The list from the 2nd to the 5th index is shown", my_list[2:5])
