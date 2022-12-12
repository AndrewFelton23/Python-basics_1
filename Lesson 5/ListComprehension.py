#List Comprehension
h_letters = []
for letters in "human":
    h_letters.append(letters)
    print("The current list is : ", h_letters)
# a condensed way of writing this for statement is shown
h_letter = [ letters for letters in "human" ]
print("The comprehension output is : ", h_letter)
    
#new number list with IF comprehension
x_numbers = [ x for x in range(20) if x % 2 == 0]
print("factors of 2 between 0 and 10 : ", x_numbers)

#new number list with nested IF list comprehension
y_numbers = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print("factors of 2 AND 5 between 0 and 100 : ", y_numbers)


#new number list with IF.. ELSE list comprehension
obj = [(i, " = EVEN") if i % 2 ==0 else (i, " = ODD") for i in range(10)]
print("ODD and EVEN numbers between 0 and 10 : ", obj)
