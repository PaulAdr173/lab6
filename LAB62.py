def mesaj():
    global alt
    alt =2
    print("h")
alt = 1
mesaj( )
print(alt)

def dis(**kwargs):
    for i in kwargs:
        print(i)

dis(emp="Kelly", salary = 900)

def add(*numere):
    total = 0
    for x in numere:
        total +=x
    return total
print(add(2, 3))
print(add(2,3,4))

def fructe(**f):
    total = 0
    for amount in f.values():
        total += amount
    return total

print(fructe(banana = 5, mango = 7))

def nume(**n):
    print(n, sep ="nota:")

nume(marian = 3, salut = 2)


a = 1
def fun():
	a = 2
	print(a)
fun()
print(a)
print("------------")
a = 1
def fun():
	global a
	a = 2
	print(a)
fun()
a = 3
print(a)
