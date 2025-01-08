elements = ["Keep", "Remove", "Keep", "Remove", "Keep","Remove", "Keep", "Remove", "Keep"]
nouvelleListe = []

for i in range(len(elements)):
    if i % 2 == 0:
        nouvelleListe.append(elements[i])

print(nouvelleListe)