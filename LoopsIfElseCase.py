



# match variable_name:
#     case 'pattern 1' : statement 1
#     case 'pattern 2' : statement 2
# ...
#     case 'pattern n' : statement n

def weekday(n):
    match n:
        case(1) : return "Monday"
        case(2) :return "Tuesday"
        case(3) :return "Wednesday"
        case(4) :return "Thursday"
        case(5) :return "Friday"
        case(6) :return "Saturday"
        case(_) :return "Sunday"
print(weekday(4))
print(weekday(6))
print(weekday(8))
# --------------------------------------------------------------






input_price = int(input("Please enter the Price of the Product: "))
match input_price:
    case 100: amount = input_price - 20
    case 500: amount = input_price - 25
    case 700: amount = input_price - 35
    case 1000: amount = input_price - 100
    case 2000: amount = input_price - 300
    case 5000: amount = input_price - 700

print("Final price of the Product is:", amount)



# ----------------------------------------------------------------

# num1 = 23.78
# num2 = 1.22
#
# num = num1 + num2
#
# print(" the sum of the numbers are :",  num )
# --------------------------------------------------------------
# Prompt user for their name
# name = input("Enter your name: ")
#
# # Prompt user for their age and convert it to an integer
# age = int(input("Enter your age: "))
#
# # Print the results
# print(f"Hello, {name}! You are {age} years old.")

# -------------------------------------------------------------

# var =100
# if (var == 100):
#     print("The number is equal to 100")
#     if(var % 2 == 0):
#         print("the number is even")
#     else:
#         print("the number is odd")
# elif var == 0:
#     print("the number is 0")
# else:
#     print("the number is negative")

# ---------------------------------------------------------

# discount =  float(input("Enter the discount Percentage"))
# amount = int(input("Enter the Price of the product: "))
# if amount > 1000:
#     Discount = amount * 10 / 100
# print("discount amount=", amount - Discount )

