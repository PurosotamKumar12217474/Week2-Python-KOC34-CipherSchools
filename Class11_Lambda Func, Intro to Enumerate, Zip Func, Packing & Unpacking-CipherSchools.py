
def func (x,y) :
    result = x+y
    return result
res = func (1, 2)
print (res)

print("")

name=['Jatin','Saransh','Shubham','Samarth']
for name in name:
    print(name)

print("")

for name in enumerate(name):
    print(name)

print("")
#Packing and Unpacking values
a=5
b=9
a,b=b,a
print(a,b) 

a=[1,2]
b,c = a
print(a)

print("")

name=['Jatin','Saransh','Shubham','Samarth']
for i,name in enumerate(name):
    print(i,"-",name)

print("")

name=['Jatin','Saransh','Shubham','Samarth']
score=['50','70','90','80']
for name,score in zip(name,score):
    print(name,score)


print("")

name=['Jatin','Saransh','Shubham','Samarth']
score=['50','70','90','80']
state=['Delhi','Punjab','Haryana','Punjab']
for name,score,state in zip(name,score,state):
    print(name,"-",score,"-",state)


print("")

