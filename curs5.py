def la_multi_ani(urari = True):
   print("Trei …")
   print("Doi …")
   print("Unu …")
   if not urari:
      return
   print("La multi ani!")

la_multi_ani()
la_multi_ani(False)

print("--------")

def exempluReturn():
   return 'abc'

text = exempluReturn()
print("Functia exempluReturn() a returnat: ", text)

print("--------")


def modPlictiseala():
   print("Mod plictiseala ON!")
   return 'abc'

print("Functiile sunt interesante!")
modPlictiseala()
print("Functiile sunt plictisitoare!")


print("--------")

def add(*numere):
    total = 0
    for x in numere:
        total += x
    return total

print(add(2, 3))
print(add(2, 3, 5))
print(add(2, 3, 5, 7))
print(add(2, 3, 5, 7, 9))


print("--------")
def fructe(**fruits):
	total = 0
	for amount in fruits.values():
            total += amount
   return total
    


print(fructe(banana=5, mango=7, apple=8))
print(fructe(banana=5, mango=7, apple=8, oranges=10))
print(fructe(banana=5, mango=7))

print("--------")
def fructe(**kwargs):
	print(kwargs)


fructe(banana=5, mango=7, mar=8)

