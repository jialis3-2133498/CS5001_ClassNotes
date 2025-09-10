# git add . 其中“ ."代表current directory，两个点代表parent directory
# Making Changes here
# Confused about how to pull and clone using git.
#  
# Identifiers: 第一个letter必须是字母，然后使用underscore来连接不同字母
# Reserved words(Key words): special meaning in Python, like "and", "for", "break", "class"
# Words used in library functions, such as "array", "open", "write", "exp", "pi"
# Words to name variables

# In Python, nameing convention is "snake_case"
# In Java, it is "camelCase"

print("Hello World")


# white space matters in Python
# "Don \' paninc" = Don't panic or 'Don \" panic"
# To print out \, we need to write it \\
# We can concatenate strings using "+" or ","
print("xyz " + "123")
print("xyz", 123) # "," gives you an extra space by default
# We can not use "+" to concatenate a string and an int, make sure they are in the same type. To avoid it, we do casting(convert int into a string)
print("xyz " + str(123))
# Use '''xxx''' or """xxx""" to expand strings in multiple lines

print("1 + 2 =", 1 + 2) # When the python read it, it excute the math first, and then the string output.
print("1 + 2 =", 1 + 2, ", You are right")
addition = 1 + 2
print(f"1 + 2 = {addition} , You are right")
print(f"1 + 2 = {addition} , You are right. \
      It is {1 + 2}")

# \n means new line, \t means tab
print("Here is a line\nHere is another line\nHere's a backslash \\")
print("""Aread and population of cities
      \tTokyo\t847 million\t220 sq miles
      \tBeijing\t9210 million\t690 sq miles""")

# In python, variables are dynamic, that means they come into existence when they are assigned to values, and we can add other type elements into it. 
# In Java, variables are static, that means we need to declare the type of one variable and we can not add other types freely. 

# Built-in data types:
#   Numeric: 
#       Integers(任何整数), 
#       Float（任何带有Decimal的数字), 
#       Complex(Imaginary Numbers)
#   Booleans: 
#       True or False
#   Sequential types: 
#       string(immutable) 
#       list(mutable): sequences of arbitrary objects
#       tuple(immutable): fixed length sequences of arbitrary objects
#       bytes(immutable): sequences of bytes
#       bytearray(mutable), sequences of bytes
#   Sets and mappings:
#       set(mutable): unordered collections of non-duplicated values
#       frozenset(immutable): unordered collections of values
#       dictionary(mutable): Mapping from one set of values(keys) to another

# String IO (Input/Output)
print("I'm a string") # To print a string to the standard output(a terminal)
my_string = input("Please type a string: ") # To read a string in from the standard input(a terminal command line)
print(f"You typed the string: '{my_string}'")

# >>> is a REPL(Read, Evaluate, Print, Loop)

# Arithmetic operations
#   +
#   -
#   *
#   \ (The result is always a float, if we use \\, it will be the int)
#   \\ Floor Division
#   % Get the remainder / Moduler
#   ** 
def main():
    num1 = float(input("Please input a number: ")) # This is the example why Python is dynamic
    num2 = float(input("Please input another number: "))
    print(f"The sum of {num1} and {num2} is {num1 + num2}")
main()

# def main2():
#     num1 = input("Please input a number: ")
#     num2 = input("Please input another number: ")
#     print(f"The sum of {num1} and {num2} is {float(num1) + float(num2)}")
# main2()

# Avoid using magic numbers in the code
def temp_converstion():
    BASE = 32
    CONVERSION_FACTOR = 5.0 / 9.0
    TEMP_PERCISION = 2 # In python, we use all cap letters to represent constants. 

    fahrenheit_temp = float(input("Input a temperature in Fahrenheit: "))
    celsius_temp = (fahrenheit_temp - BASE) * CONVERSION_FACTOR
    print(f"Result: {round(celsius_temp, TEMP_PERCISION)} degrees celsius")
temp_converstion()


# def quadratic_formula():
#     PRECISION = 3
#     a = float(input("Please input the coefficient of the x squared: "))
#     b = float(input("Enter the coefficient of x: "))
#     c = float(input("Enter the constant: ")) # nameing variables using a, b, c is not bad because the formula is universal. 

#     TWO = 2
#     FOUR = 4
#     discriminant = b ** TWO - (FOUR * a * c)
#     root1 = ((-b) + sqrt(discriminant)) / (TWO * a)
#     root2 = ((-b) - sqrt(discriminant)) / (TWO * a)

#     print("Root #1: ", round(root1, PRECISION))
#     print("Root #2: ", round(root2, PRECISION))
# quadratic_formula()



