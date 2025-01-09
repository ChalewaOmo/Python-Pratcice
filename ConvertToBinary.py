def convertBinary(oldnumber) :
    if oldnumber < 0 :
        number = abs(oldnumber)
        binary = str(number)
        binary = binary.replace("0b"," ")
        print(f"{number} -> {binary} (because {oldnumber} is {bin(number)} in binary)")
        
    else :

        binary = str(oldnumber)
        binary = binary.replace("0b"," ")
        print(f"{oldnumber} -> {bin(oldnumber)} because {oldnumber} is 0b{bin(oldnumber)} in binary")

oldnumber = int(input("Enter a negative number: "))
convertBinary(oldnumber)