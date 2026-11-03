filepath = "C:/Users/ROG/Downloads/clone/input.txt"
with open(filepath, "r") as file:
    conten = file.read().split(',')
    print(conten)