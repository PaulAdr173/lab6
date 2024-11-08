def mesaj():
    print("Introduceti o valoare:")

print("Start")
mesaj()
print("Stop")

print("--------")

#definirea functiei
def salut(nume):
   print("Salut,", nume)


nume = input("Introduceti numele:")

prenume = nume.split(" ")[1]
#apelul functiei
salut(nume)
print(prenume)

print("--------")

def salut(nume):
   print("Salut,", nume)

nume = "Damian"
prenume = input("Introduceti prenumele:")
salut(prenume)
print(nume)



def salut(nume, prenume):
   print("Salut,", prenume, nume)

nume = input("Introduceti numele: ")
prenume = input("Introduceti prenumele: ")

salut(nume, prenume)
salut(prenume, nume)
