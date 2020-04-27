a=2+3

b=a**5

"""

/ forward slash as it is falling forward

\ backward slash falling backwards

for every special character we have to use

'\' back slashes known as escape sequences

\n

\t

"""

#//////////////////////////////////

print("hello world")

a="hello "

print(a*4+" :::: too much of hellooo " )

a="2"+"3"

print(a)

type(a)

#a+5

print(int(a)+5)

input("Lets enter here something : ya ya here :::: ")

#this is not stored any where so lets store it somewhere

a=input("Lets just take the life of a : Yes or No ::: ")

b=input()

#///loops and Conditionals

if(a=="Yes"):

print("'a' must have to die now ")

elif(a=="No"):

print("let the 'a' live ")

else:

print("Input was wrong now you have to die")

#the naming of variables should be simple and easy to understand a_normal_variable_name ="this is correct"

q123abc="not a valid name"

#a b c= 123

#multiple initialsation in python

a,b,c=1,2,3

a=1

a=a+3

print(a)

a+=3

print(a)

a="apple is "

a+="a smart fruit"

print(a)

#splitting and slicing

print(a[0])

print(a[1])

print(a[0:])

print(a[1:6])

print(len(a))

print(a[0:len(a):2])

"""

a[start:end point : interval ]

apei mr ri

"""

print(a[0:len(a):3])

#boolean

totalFalse=True

totalFalse = (2==2)

if totalFalse:

print("You are true")

else:

print("your statement is not true so lets take it as false :-)")

#//boolean logics

if 1==1 and 2==2:

print("both are true")

if 1==2 or 2==2:

print("one of them is false: still true")

if not(1 == 2) :

print("it is NOT correct")

#//Loopsssss

a=10

while a>0:

print(a)

a-=1

a="the most commonly used variable"

for i in range(len(a)):

print(a+str(i))

for i in range(len(a)):

print(i) for i in range(len(a)):

print(a[i])

i=20

while i:

print("a",end=' ')

i-=1

#list = an object in python that is used to store indexed list of items

list=[]

list.append("an")

list.append("apple")

list.append("a")

list.append("day")

for list_val in list:

print(list_val,end=" ")

list.reverse()

for list_val in list:

print(list_val,end=" ")

list.append(2)

list.append(9)

for list_val in list:

print(list_val,end=" ")

list1=[3,2,1]

list2=[4,5,6]

print(list1)

print(list2)

list1.reverse()

print(list1)

# just like strings

list1+=list2

print(list1)

list1.remove(4)

list1.insert(0,4)

print(list1)

list1.sort()

print(list1)

list1.index(5)

max(list1)

#functions and importing modules in python

"""

WET- write everything twice (we enjoy typing)

DRY- Dont Repeat Yourself

"""

def add_strange(a):

a+=" strange "

print("strange is added now")

a="my name is mister"

print(a)

add_strange(a)

print(a)

a="my name is doctor"

print(a)

def add_strange(b):

global a

a+=" strange"

print("strange is added now")

add_strange(a)

print(a)

def print_in_style(word):

return "heyy this is a {} ".format(word)

a="happy"

result = print_in_style(a)

print(result)

#//classses

"""

Python is an object oriented programming language.Almost everything in Python is an object, with its properties and methods.A Class is like an object constructor, or a "blueprint" for creating objects.

"""

class danceParty:

dancers=5

guests=20

waiters=8

class kittyParty:

dancers=0

guests=10

waiters=2

class weddingParty:

dancers=25

guests=200

waiters=28

birthday=danceParty()

promotion=kittyParty()

marriage=weddingParty()

total_dancers = birthday.dancers + promotion.dancers + marriage.dancers print(total_dancers)

if(marriage.guests>150):

print("book a larger venue")

else:

print("smaller one is okay")

marriage.guests=100

dancers_cost=0

while weddingParty.dancers>0:

dancers_cost+=100

weddingParty.dancers-=1

print("dancers cost for wedding party is '{}' ".format(dancers_cost))

#//since it isnt having any init() funtion so it wont execute and command when the object is called

#print(birthday())

class bio_data:

def __init__(self,name,age):

self.name=name

self.age=age

def child(self):

self.age=5

def adult(self):

self.age=18

def increase20(self):

self.age+=20

person1=bio_data("Rohan",40)

print("\n\n\nThe age of person is '{}' and the name is '{}'".format(person1.age,person1.name))

person2=bio_data("Deepak",0)

print(" before executing the function ",end=" ")

print(person2.age)

person2.adult()

print(" after executing adult function ",end=" ")

print(person2.age)

person2.child()

print(" after executing child function ",end=" ")

print(person2.age)

person2.increase20()

print("after executing increment of 20 ",end=" ")

print(person2.age)

person2.increase20()

print("after executing increment of 20 two times ",end=" ")

print(person2.age)
