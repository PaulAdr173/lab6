
def exempluReturn():
   return 'abc'

text = exempluReturn()
print("Functia exempluReturn() a returnat: ", text)


def modP():
   print("Mod plictiseala ON!")
   return 'abc'

print("1")
modP()
print("2")
print("--------------------------")

def add(*n):
    total =0
    for i in n:
        total +=i
    return total

print("Suma:",add(1,2,4,5,5,5,5,5,5))

def add(*n):
    cont = 0
    sum = 0
    for i in n:
        cont += 1
        sum +=i
    imp= sum //cont
    return imp

print("Impartire:",add(1,2,3))

print("--------------------------")
def med(**nota):
    cont = 0
    sum = 0
    for i in nota.values():
        cont += 1
        sum += i
    imp= sum /cont
    return imp

print("Media 1cls:",med(Maria=9, Andrei=7, Ioana=8, Mihai=10, Elena=6, Radu=8))
print("Media 2cls:",med(Maria=9, Andrei=7, Ioana=8, Mihai=10, Elena=6, Radu=8, Alex=10, Bianca=5))
print("Media 3cls:",med(Maria=9, Andrei=7, Ioana=8, Elena=6))
