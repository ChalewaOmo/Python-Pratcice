elements = ["Keep", "Remove", "Keep", "Remove", "Keep","Remove", "Keep", "Remove", "Keep"]
elements = [element for index, element in enumerate(elements) if index % 2 == 0]
print(elements)