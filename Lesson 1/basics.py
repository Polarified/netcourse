# Python doesn't care what type a variable is.
x = 1
x = "a"
x = 1.0
x = True

# Input and output
user_input = input("Enter your input...")
print(user_input)

# Operators
print(1 + 2)
print("a" + "b")
print(1 / 7)
print(1 // 7)
print(4 * "a")

# Conditionals
number = int(input("Enter a number"))
if number < 5:
    print("Smaller than 5!")
elif number == 5:
    print("Number is 5")
else:
    print("Greater than 5")

# Lists and Tuples
x = [1, 2, 3, 4, 5, 6, 7]
y = list(range(1, 7, 2))
z = x[1:6]
print(x, y, z)
x[0] = 0
print(x)
x.append(8)
print(x)
a = ("A", "B", "C")
# This is going to fail
try:
    a[0] = "Z"
except:
    print("You cant do that!")

# Loops
# Which is the best?
for i in x:
    print(i)

for i in range(len(x)):
    print(x[i])

i = 0
while i < len(x):
    print(x[i])

# Sets & Dicts
s = {1, 2, 3, 3, 2, 1}
print(s)
d = {"apple": 2, "banana": 4, "orange": 6}
print(d)
print(d["apple"])

# Comprehensions
l = [x ** 2 for x in range(20)]
d = {k: k ** 2 for k in range(20)}
print(l, d)


# Functions
def multiply_by_2(param):
    return param * 2


# That's it! If you understand what each thing here does, you should be fine with the code we write.
# The most important part will be to read code and understand, later you can get better at writing your own!