def lma(urari = True):
   print("TRei")
   print("doi")
   print("unu")
   if not urari:
      return
   print("La multi ani!")


lma()
lma(0)
print(lma(1))

def fnone(n):
   if(n % 2 == 0):
      return True

print(fnone(2))
print(fnone(3))