#Jump statements are those like break and continue

#the Break condition in numbers
n = [1,2,3,4,5,6,7,7,6,5,3,4,24,123,43,234]
d = float(input('Enter a value to check if it is in the list: '))
for c in n:
    if d == c:
        print(d, ' found')
        break
    if c == n[-1]:
        print(d, ' not found')

#the break condition in strings
#create a string variable
st = "string"
#get input from the user and store it in a variable
b = input('Check if a character is in the string: ')
#use a for loop
for e in st:
    if e == b:
        print('found the value ',e)
        break
    if e == st[-1]:
        print('char not found')

#the continue jumpstatement
#Get input from the user and store it in a variable
b = input('Remove a character from the string: ')
#create a new empty string variable
f = ''
for e in st:
    if e == b:
        #skip the character
        continue
    #if the desired value is not the current character then add it to the string
    f = f + e
#print the final string without the value
print(f)
    

    
