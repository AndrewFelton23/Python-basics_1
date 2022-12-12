#Two kinds of loops namely for loops and while loops

#create a list of numbers
n = [1,2,3,4,5,6,7,7,6,5,3,4,24,123,43,234]
s = 0;
#for loop
for c in n:
    print(c,' current value')
    s = s+c
    print(s, ' summed value')

#while loop
a = 0
b = float(input('Enter a value to sum: '))
s = 0
while a <= b:
    s = s + a
    print(s)
    print('condition not met')
    #increment the check variable
    a = a + 1
print('condition met')


    

