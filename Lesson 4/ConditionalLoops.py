#conditional loops basic

n = -3

if n > 0:
    print(n,' is greater than zero')
else:
    print(n,' less than zero')
#get input from user and store it
g = float(input('Enter a number`; '))
#check if enter number is greater than n 
if g > n:
    print('Entered value is correct')
    if g == 0:
        print('number is zero')
    else:
        if g > 0:
            print('number is positive')
        else:
            print('number is negative')
else:
    print('Entered value is too small')
