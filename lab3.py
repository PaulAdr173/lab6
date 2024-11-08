def isAnBisect(an):
    an = int(input("Introduceti un an:"))
    if((an % 4 == 0) and ((an % 400 == 0) or not(an % 100 == 0))):
        return True
    else:
        return False

isAnBisect(an=2000)

    
