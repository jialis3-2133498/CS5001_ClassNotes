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

def main():
    print("Hello CS 5001 pioneers!")
main()

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

# In python, variables are dynamic, that means they come into existence when they are assigned to values. 
# In Jave, variables are declaritive, that means we need to 



