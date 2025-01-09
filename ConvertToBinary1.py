def convertBinary(oldnumber):
    if oldnumber < 0:
        number = abs(oldnumber)
        binary = bin(number)[2:]  # Convertir en binaire et supprimer le préfixe "0b"
        return f"{number} -> {binary} (because {oldnumber} is {bin(number)} in binary)"
    else:
        binary = bin(oldnumber)[2:]  # Convertir en binaire et supprimer le préfixe "0b"
        return f"{oldnumber} -> {binary} because {oldnumber} is 0b{binary} in binary"

oldnumber = int(input("Enter a negative number: "))
result = convertBinary(oldnumber)
print(result)  # Affiche uniquement la chaîne retournée
