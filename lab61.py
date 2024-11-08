def fructe(**fruits):
    total = 0
    for amount in fruits.values():
        total += amount
    return total

print(fructe(banana=5, mango=7, apple=8))
print(fructe(banana=5, mango=7, apple=8, oranges=10))
print(fructe(banana=5, mango=7))

def ist(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(ist(5))
print(ist(5.0))
print(ist("5"))

def listu(lst):
    upList=[]
    for elem in lst:
        elem **= 2
    upList.append(elem)
    return upList

I = [1,2,3,4,5]
print(listu(I))
i = 0
for i in I:
    print(listu(I))
