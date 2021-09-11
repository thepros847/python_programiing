txt = "I like bananas"

x = txt.replace("bananas", "mangoes")

print(x) 


txt = "one one was a race horse and two two was one too."

x = txt.replace("one", "three")

print(x) 


txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 1)

print(x) 


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) 


txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36) 



txt = "banana"

x = txt.center(15)

print(x) 


txt = "banana"

x = txt.center(20, "/")

print(x) 



txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x) 



txt = "Hello, And Welcome To My World!"

x = txt.upper()

print(x) 


txt = "Company12"

x = txt.isalnum()

print(x) 


txt = "Company!@#$"

x = txt.isalnum()

print(x) 



txt = "welcome to the jungle"

x = txt.split()

print(x) 



txt = "hello? my name is Peter? I am 26 years old"

x = txt.split("?")

print(x) 



txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x) 


