#Arrays
#creating the array it must be imported
import array as arr
a = arr.array("I",[3,6,9])
#printing a element from the array
print(a[0])
#Finding the size in bites of one array item
print(a.itemsize)
#Append the array with a new item x
x = 5
print('array before item appended: ',a)
a.append(x)
print('array after item appended: ',a)
#finding the number of times a certain item appears in the array
x = 3
print(x, ' appears ', a.count(x),' times')
#finding the first occurance of a element in the array
try:
    x = int(input("Enter a number to find: "))
except:
    print('Please enter a integer')
else:
    try:
        print(x, ' first occurance is at position ', a.index(x),' in the array')
    except:
        print('Value not found')
#insert a item at a specific position
b = 7
c = 2
print('array before item inserted: ',a)
a.insert(c,b)
print('array after item ',b,' inserted at position',c,': ',a)
#remove the first item from the array with a sepcific value
b = int(input("Enter a number: "))
print('array before item removed: ',a)
a.remove(b)
print('array after item ',b,' removed: ',a)
#reverse the order of items in the array
print('array before reversed: ',a)
a.reverse()
print('array after reversed: ',a)


