def fructe(**fructe):
    total = 0
    for i in fructe.values():
        total += i
    return total
print(fructe(banana = 7, mango = 7))
print(fructe(banana = 5, mango = 7, apple = 8))
 