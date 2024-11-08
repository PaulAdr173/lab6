def hi(title = "dl.", firstName, lastName):
   print("Salut,", title, firstName, lastName)


def hi(firstName, lastName, title="dl."):
   	print("Salut,", title, firstName, lastName,'!')

nume = input("Introduceti numele: ")
prenume = input("Introduceti prenumele: ")

hi(prenume, nume)
hi(title = "dr.", lastName = nume, firstName = prenume)
