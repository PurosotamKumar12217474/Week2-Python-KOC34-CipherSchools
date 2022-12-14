#def Function
def show_loading():
    for _ in range(3):
        print("loading...")
a=5
b=7
print(a+b)
show_loading()
print(a-b)
show_loading()
print(a*b)
show_loading()

def sheldon_knock():
    for _ in range(3):
        print("Knock Knock Knock Penny")
sheldon_knock()
print("\n")

def sheldon_knock(name):
    for _ in range(3):
        print("Knock Knock Knock",name)
sheldon_knock("Leonard")
print("\n")

def sheldon_knock(name,times):
    for _ in range(times):
        print("Knock Knock Knock",name)
sheldon_knock("Leonard", 10)

#Return Statement
def add(a,b):
    return a+b
a=add(1,2)
print(a)