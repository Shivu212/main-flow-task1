print("SHIVANI PRAJAPATI")
# how to declare a variable
a=2
b=2
c=a+b# 
print(c)

#different operations perform on a list
list= [93,4,7,8,9,12,34]
print(list)
# check the data type
print (type(list))
# popping the first element
list.pop(0)
print(list)
# appending new value into the list
list.append(46)
print(list)
# changing the element at 0 index
list[0]=24
print(list)
# reversing element of a list
list.reverse()
print(list)

# different operations perform on a tuple
tup1=(1,4,'ant','true',7,4,3.14)
print(tup1)
#check the data type of the object
print(type(tup1))
# how to extract individual element from a tuple
print(tup1[-1])
print(tup1[2])
# how to create an dictionary and perform different operations on a dictionary
d1={"car":25,"bus":28,"jeep":15,"bike":60}
print(d1)
# extrating keys and values
print(d1.keys())
print(d1.values())
# modifying a dictionary
d1["cycle"]=32
print(d1)
d1["bus"]=50
print(d1)
#update one dictionary's element with another
d2={"truck":16,"trump":12}
print(d1.update(d2))
print(d1)
# popping an element
d1.pop("trump")
print(d1)
#a code using loops
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
# a code for simple calculator using fuctions
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")