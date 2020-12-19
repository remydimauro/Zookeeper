atoms = int(input())
final_atoms = int(input())
days = 0
while atoms >= final_atoms:
    days += 12
    atoms = atoms / 2
print(days)
