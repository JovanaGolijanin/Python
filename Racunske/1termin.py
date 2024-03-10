""" if 2 > 1:
    print("Dva je veće od jedan!")
    #slogiracu od faksa
x = 10
print(type(x)) 
print(id(x))
y = 'tekst'
print(type(y))
print(id(y))

print(10 > 9) 
print(10 == 9) """
""" 
print(bool("abc") )
print(bool(123)) 
print(bool(["o1", "o2", "o3"]) )
print(bool(False))
print(bool(None) )
print(bool(0) )
print(bool("") )
print(bool(()) )
print(bool([]) )
print(bool({}))

x = 'ovo je string'
y = "Ovo je string"
z = '''I ovo je string'''
print(type(x) )
print(x) 
a = "Hello, World!"
print(a[1]) 
print(len(a)) 
print("hello" in a)
print("Hello" in a) 
print("hello" not in a)
print(a[2:5])
print(a[:5]) 
print(a[7:])
print(a[-5:-2])
print(a.upper()) 
print(a.lower()) 
print(a.replace("W", "w")) 
print(a.split(","))  """

""" a = "Hello"
b = "World"
c = a + " " + b
print(c) 
print(a*2) 
#d = a + 2 
d = "ona ima {} godina".format(10)
print(d) 
d = "%s %d" % (a,2)
print(d) 
print(f'{"Ona"} ima {10} godina')  """

""" list1 = ["jabuka", "banana", "kruska"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, [1, 5]]
# Pristup elementima liste po indeksu:
print(list1[1]) #-> banana
print(list1[-1]) # -> kruska
print(list4[1:4]) # -> [34, True, 40]

if "jabuka" in list1:
    print("Da")
list1[1] = "mango"
print(list1)

list1.append("breskva")
print(list1)
list1.insert(1, "breskva")
print(list1)
list1.remove("breskva") 
print(list1)
list1.pop(1) 
print(list1)

list1.clear() 
print(list1) """

""" list1 = ["jabuka", "mango", "banana", "kruska"]
list1.reverse()
print(list1)
list1.sort()
print(list1) 
list1.sort(reverse = True)
print(list1) 

list5 = list1.copy()
print(list5)  """

""" 
tuple1 = ("jabuka", "mango", "banana", "kruska")
tuple2 = ("jabuka", [1,2,3], "banana", "kruska")
tuple3 = (12, 13, 14)
tuple4 = ("jabuka",)# kreiranje tuple-a sa jednim elementom
nottuple = ("jabuka")# ovo je string 
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(nottuple)

print(tuple2[2])
print(len(tuple2)) 

#tuple2[0]="breskva" # vraća grešku – elementi ne mogu da se menjaju
tuple2[1][0] = 5
print(tuple2)

y = ("breskva",)
tuple2 += y

print(tuple2) """

""" dict1 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"colors": ["red", "white", "blue"]
} """

""" x = dict1.keys()
print(x) 

y = dict1.values()
print(y)

z = dict1.items()
print(z) """

""" x = dict1["model"] #-> Mustang
print(x)
x = dict1.get("model")
print(x)

print(len(dict1))

dict2 = dict1.copy() 
print(dict2)

dict1.clear()
print(dict1)

del(dict1)
#print(dict1) """

""" set1 = {"jabuka", "banana", "kruska"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40}
print(type(set1)) 

for x in set1:
    print(x)

print("banana" in set1)

set1.add("breskva")
print(set1)

set1.update(set2)
print(set1)

set1.remove(3)
print(set1)

set1.clear()
print(set1)

#del set1
print(set1) """

""" a = 10
b = 7
if b > a:
    print("b je veće od a")
elif a == b:
    print("a i b su jednaki")
else:
    print("a je veće od b") """

""" a = 10
b = 7
c = 5
if a > b and b > c:
    print("Poredak je dobar") """

""" lista= ["o1", "o2", "o3"]
for x in lista:
    print(x)

for x in "tekst":
    print(x)

for x in lista:
    print(x)
    if x == "o2":
        break

for x in lista:
    if x == "o2":
        continue
    print(x) """

""" for x in range(4):
    print(x)

for x in range(3, 12, 3):
    print(x) """

""" for x in range(4):
    print(x)
else:
    print("kraj!")


for x in range(4):
    if x == 3:
        break
    print(x)
else:
    print("kraj!")

i = 1
while i < 6:
    print(i)
    i += 1 """

""" i = 1
while i < 4:
    print(i)
    if i == 2:
        break
    i += 1 """

""" i = 0
while i < 4:
    i += 1
    if i == 2:
        continue
    print(i) """
    
""" i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("i nije manje od 4")

i = 0
while i < 4:
    if i == 2:
        break
    print(i)
    i += 1
else:
    print("i nije manje od 4") """

""" def func1():
    print("Hello world!")
func1() #-> Hello world!

def hello(param1='hello',param2='world'):
    print('%s, %s!' % (param1, param2))

hello() #-> hello, world!
hello('Hi') #-> Hi, world!
hello('Nice','day') #-> Nice, day!
hello(param2='everyone')# -> hello, everyone! """

""" 
def stampa(lista):
    for x in lista:
        print(x)

fruits = ["jabuka", "banana", "kruska"]
stampa(fruits) """


def proizvod(x, y):
    return x * y
valX = input("Unesite vrednost za x: ")# -> Unesite vrednost za x: 5
valY = input("Unesite vrednost za y: ") #-> Unesite vrednost za y: 6
print(proizvod(int(valX),int(valY))) 

