#the else statement paired with the for and while loops
#Declare two variables that will hold a user input and the desired input
ToGuess = 5
guess = 0

#open the while loop
while guess != ToGuess:
    guess = int(input("Please enter a positive number: "))
    #check if the entered number is positive
    if guess > 0:
        #check if the entered number is greater or less than the desired value
        if guess > ToGuess:
            print("The number is too large.")
        elif guess < ToGuess:
            print("The number is too small.")
    else:
        print("Thank you for trying")
        break
else:
    print("Congratulations you guessed right")

#Declare a list of strings
ShoppingList = ["Eggs","Bread","Honey","Milk","Sugar","Chips"]
#Take user input
NN = input("Enter a value that you don't want.")
for food in ShoppingList:
    if food == NN:
        print("No more ", NN," thanks.")
        break
    print("Thank you for getting ", food)
else:
    print("Thank you for not getting eggs.")
print ("That concludes the shopping experience")

