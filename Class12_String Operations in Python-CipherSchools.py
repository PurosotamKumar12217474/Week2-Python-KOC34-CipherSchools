a=5
print("Value of a is %d"%(a))
print("Value of a is {}".format(a))
a="Jatin"

a,b,c,d=1,2,3,4
print("a={},b={},c={},d={}".format(a,b,c,d))
print("a={},b={},c={},d={}".format(b,d,c,a))

print("")

name="Jatin Katyal"
company="Shruttl"
print("Hello my Name is {name} and I work at company={company}".format(name=name,company=company))

print("")

print(f"Name={name}")

print("")

print(len("a\nb"))
print(len(r"a\nb"))

print("")

for c in "a\nb":
    print(c)

print("")

for c in r"a\nb":
    print(c)

a="     Jatin   *".strip()
print(a)
a="1,2,3,4,5".split(",")
print(a)

a="Jatin Katyal".replace("a","z")
print(a)