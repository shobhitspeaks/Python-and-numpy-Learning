# 1 - write a programm to make dictionary hindi words translate
# into english words:
words = {
    "Kaise ho": "How are you",
    "Mai acha hu" : "I'm Fine",
    "Chalo Baad me Baat Karta Hu" : "I'll Talk to later"
}
word = input("enter your words:")
print(words[word])

# 2 - write a programm to input eight numbers from the users and
# display into unique numbers:
s = set()
num1 = int(input("Enter your number1:"))
s.add(num1)
num2 = int(input("Enter your number2:"))
s.add(num2)
num3 = int(input("Enter your number3:"))
s.add(num3)
num4 = int(input("Enter your number4:"))
s.add(num4)
num5 = int(input("Enter your number5:"))
s.add(num5)
num6 = int(input("Enter your number6:"))
s.add(num6)
num7 = int(input("Enter your number7:"))
s.add(num7)
num8 = int(input("Enter your number8:"))
s.add(num8)

print(s)

# 3- what is the length of the following set:
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))

# 4 - emplty dictionary language:
d = {}
name = input("enter your name: ")
lang = input("enter your language: ")
d.update({name : lang})

name = input("enter your name: ")
lang = input("enter your language: ")
d.update({name : lang})

name = input("enter your name: ")
lang = input("enter your language: ")
d.update({name : lang})

name = input("enter your name: ")
lang = input("enter your language: ")
d.update({name : lang})

print(d)