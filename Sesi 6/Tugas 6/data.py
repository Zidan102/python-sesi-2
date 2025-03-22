name = "Nugraha", "john   ", "Jane   ", "Doe    "
yearnow = 2025
birthdate = yearnow - 1989, yearnow - 1990, yearnow - 1992, yearnow - 1994
print('No     | Name     | Age  |')
for i, (x,y) in enumerate(zip(name,birthdate)):
    print(i+1,"     |",x," |",y,"  |")