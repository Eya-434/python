num1 = 42   #variable declaration,initialize numbers
num2 = 2.3  #variable declaration,initialize numbers
num3 = 72
print(num3)
boolean = True  #data type boolean
string = 'Hello World'  #variable declaration,initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #data type composite :list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #data type composite :dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana')    #data type composite :tuple initialize
print(type(fruit))    #type check
print(pizza_toppings[1])  #data type composite :list access value
pizza_toppings.append('Mushrooms')  #data type composite :list add value
print(person['name'])      #data type composite :dictionary access value
person['name'] = 'George'  #data type composite :dictionary change value
person['eye_color'] = 'blue'  #data type composite :dictionary add value
print(fruit[2])       #data type composite :tuple access value

if num1 > 45:                    # conditional if else 
    print("It's greater")           
else:
    print("It's lower")          

if len(string) < 5:                 # conditional, if else, if ,else
    print("It's a short word!")          
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")          

for x in range(5):             #for loop
    print(x)                     #for loop
for x in range(2,5):            #for loop
    print(x)                     #for loop
for x in range(2,10,3):          #for loop
    print(x)  
x = 0
while(x < 5):                      #while loop
    print(x)
    x += 1

pizza_toppings.pop()          #data type composite :list delete the last value
pizza_toppings.pop(1)          #data type composite :list delete  value 1

print(person)
person.pop('eye_color')       #data type composite :dictionary delete value
print(person)

for topping in pizza_toppings:     # for loop start
    if topping == 'Pepperoni':      #conditional if
        continue                     #conditional if continue
    print('After 1st if statement')
    if topping == 'Olives':           #conditional if
        break                     #conditional if break

def print_hello_ten_times():    #function parameter
    for num in range(10):       #for loop
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):    #function parameter
    for num in range(x):        #for loop
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):     #function parameter
    for num in range(x):                     #for loop
        print('Hello')

print_hello_x_or_ten_times()            
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)