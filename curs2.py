
def salut(nume, prenume):
   print("Salut,", prenume, nume)

nume = input("Introduceti numele: ")
prenume = input("Introduceti prenumele: ")

salut(nume, prenume)
salut(prenume, nume)


print("--------")


def salut(nume, prenume):
   print("Salut,", nume, prenume, sep="-")

nume = input("Introduceti numele: ")
prenume = input("Introduceti prenumele: ")

salut(nume, prenume)
salut(prenume = prenume, nume = nume)