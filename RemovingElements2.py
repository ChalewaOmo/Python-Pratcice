elements = ["Keep", "Remove", "Keep", "Remove", "Keep","Remove", "Keep", "Remove", "Keep"]
nouvelleListe = []

for index, element in enumerate(elements):
    if index % 2 == 0:
        nouvelleListe.append(element)

print(nouvelleListe)
    
