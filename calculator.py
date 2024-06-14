#1. The Calculator App
#Task 1: Create functions for each arithmetic operation, with parameters for two numbers to be used in the operation. 
#Task 2: Implement user input to receive numbers and an operation choice, their response for operation should call the associated function.

import math

def add_nums(num_1,num_2):
    res = num_1 + num_2
    print(f"Sum of the numbers provided is {res}!!")

def subtract_nums(num_1,num_2):
    res = num_1 - num_2
    print(f"Difference of the numbers provided is {res}!!")
    
def multiply_nums(num_1,num_2):
    res = num_1 * num_2
    print(f"Product of the numbers provided is {res}!!")

def divide_nums(num_1,num_2):
    res = num_1 / num_2
    print(f"The result of the division operation is {res}!!")

def mod_nums(num_1,num_2):
    res = num_1 % num_2
    print(f"The result of the mod operation is {res}!!")

def pow_nums(base,expo):
    res = math.pow(base,expo)
    print(f"The result of the power operation is {res}!!")

def log_nums(num_val,base_val):
    res = math.log(num_val,base_val)
    print(f"The result of the log operation is {res}!!")

def cosine_value(degree):
    res = math.cos(math.radians(degree))
    print(f"Cosine of entered value is {res}!!")

def sine_value(degree):
    res = math.sin(math.radians(degree))
    print(f"Sine of entered value is {res}!!")

# is responsibly for driving my code
# this is where the while loop will live
# and it will also call all my other functions
def main():
    print("""
    Please choose operation from the list below:
          1. Perform Addition operation using Calculator(type add)
          2. Perform subtraction operation using Calculator(type subtract)
          3. Perform multiplication operation using Calculator(type multiply)
          4. Perform Division operation using Calculator(type divide)
          5. Perform Mod operation using Calculator(type mod)
          6. Advanced Operations:(type advan)
             1.Trignometric Functionality(type trig)
             2.Exponential Functionality(type expo)
             3.Logarithmic Functionality (type log)
          7. Type exit to quit from this operation
        """)
    while True:
        operation = input("What would you like to do? Provide your input ").lower()
        # conditionals to check the user response and call the necessary functions
        if operation == "add":
            num_one = int(input("Enter num1 whose sum you want to calculate "))
            num_two = int(input("Enter num2 whose sum you want to calculate "))
            add_nums(num_one,num_two)

        elif operation == "subtract":
            num_one = int(input("Enter num1 for performing subtraction "))
            num_two = int(input("Enter num2 for performing subtraction "))
            subtract_nums(num_one,num_two)

        elif operation == "multiply":
            num_one = int(input("Enter num1 whose product you want to calculate "))
            num_two = int(input("Enter num2 whose product you want to calculate "))

            multiply_nums(num_one,num_two)
        
        elif operation == "divide":
            num_one = int(input("Enter num1 (dividend)for executing division operator "))
            num_two = int(input("Enter num2 (divisor) for performing division "))

            if num_two == 0:
                print("Please enter new number for num2, as you will encounter divide by zero error")
                continue

            divide_nums(num_one,num_two)
        
        elif operation == "mod":
            num_one = int(input("Enter num1 to calculate mod result "))
            num_two = int(input("Enter num2 to calculate mod result "))

            mod_nums(num_one,num_two)

        elif operation == "advan":
            print(""" Following operations are supported!!
                  1. Type trig for sin and cos calculation
                  2. Type expo for calculating power of a number
                  3. Type log to find log value of a number 
                  """)
            
            operation = input("Provide your input for the operation(log/expo/trig)").lower()
            if operation == "expo":
                num_one = int(input("Enter num1 for base! "))
                num_two = int(input("Enter num2 for exponent! "))

                pow_nums(num_one,num_two)

            elif operation == "log":
                num_one = int(input("Enter num1 for base! "))
                num_two = int(input("Enter num2 for exponent! "))

                log_nums(num_one,num_two)

            elif operation == "trig":
                num_one = int(input("Enter value in degrees for finding cosine!"))
                num_two = int(input("Enter value in degrees for finding sine!"))
                cosine_value(num_one)
                sine_value(num_two)

        elif operation == "exit":
            print("You have chosen to exit/quit the session! Have a great time!")
            break
        else: 
            print("Please choose a valid option add/subtract/multiply/divide/advanced(trig/expo/log) or exit to quit")

main()