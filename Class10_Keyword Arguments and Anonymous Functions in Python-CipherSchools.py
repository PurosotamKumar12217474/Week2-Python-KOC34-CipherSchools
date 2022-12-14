print(1,2,3,4,5, sep=",")

def hello():
    print("Hello world!")
a=1
a=hello
a()

#Arguments in python
#Required Arguments
def func(a,b):
    print(a,b)
func(1,2)

print("")

#Default Arguments
def func(a=1,b=2):
    print(a,b)
func()
func(1)
func(3,4)

print("")

#Optional Arguments
def func(*a):
    print(a)
func(1,2,3,4)

print("")

def func(a,b,*c):
    print(a)
    print(b)
    print(c)
func(1,2,3,4,"Jatin",1.5)

print("")

#Required Keyword only arguments
def func(a,b,*c,d):
    print(a)
    print(b)
    print(c)
    print(d)
func(1, 2, 3, 4, 5, 6, 7, d=8)

print("")

#Required Keyword only arguments
def func(a,b,*c,d,e="Jatin"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func(1, 2, 3, 4, 5, 6, 7, d=8)

print("")
#Default Keyword only arguments
def func(a,b,*c,d,e="Jatin"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func(1, 2, 3, 4, 5, 6, 7, d="Something", e="asdf")

print("")
#Optional Keyword only arguments
def func(a,b,*c,d,e="Jatin"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func(1, 2, 3, 4, 5, 6, 7, d="Something", e="asdf")

print("")
#Optional Keyword only arguments
def func(**k):
    print(k)
func(name="1,2,3")

print("")
#Anonymous Function or Lambda Function
lamb=lambda a,b: a+b
print(lamb(1,2))
