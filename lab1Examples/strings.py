#example1
print("Hello")
print('Hello')

#example2
a = "Hello"
print(a)

#example3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#example4
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#example5
a = "Hello, World!"
print(a[1])

#example6
for x in "banana":
    print(x)

#example7
a = "Hello, World"
print(len(a))

#example8
txt = "The best things in life are free!"
print("free" in txt)

#example9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#example10
txt = "The best things in life are free!"
print("expensive" not in txt)

#example11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#example12
b = "Hello, World!"
print(b[2:5])

#example13
b = "Hello, World!"
print(b[:5])

#example14
b = "Hello, World!"
print(b[2:])

#example15
b = "Hello, World!"
print(b[-5:-2])

#example16
a = "Hello, World!"
print(a.upper())

#example17
a = "Hello, World!"
print(a.lower())

#example18
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#example19
a = "Hello, World!"
print(a.replace("H", "J"))

#example20
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#example21
a = "Hello"
b = "World"
c = a + b
print(c)

#example22
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#example23
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#example24
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#example25
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#example26
txt = "We are the so-called \"Vikings\" from the north."

#exmaple27

