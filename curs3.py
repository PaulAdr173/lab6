def hi(title, firstName, lastName):
   print("Salut,", title, firstName, lastName)
titlu = input("Introduceti forma de apel: ")
nume = input("Introduceti numele: ")
prenume = input("Introduceti prenumele: ")

hi(titlu, prenume, nume)
hi(titlu, nume = nume, prenume = prenume)
hi(lastName = nume, firstName = prenume, title = titlu)
hi(nume, firstName = prenume, title = titlu)
