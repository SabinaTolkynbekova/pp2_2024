#example1
x = 5
y = "John"
print(x)
print(y)

#example2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#example3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#example4
x = 5
y = "John"
print(type(x))
print(type(y))

#example5
x = "John"
# is the same as
x = 'John'

#example6
a = 4
A = "Sally"
#A will not overwrite a

#example7
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#example8
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#example9
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#example10
x = "Python is awesome"
print(x)

#example11
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#example12
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#example13
x = 5
y = 10
print(x + y)

#example14
x = 5
y = "John"
print(x, y)

#example15
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#example16
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#example17
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#example18
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#example19
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
