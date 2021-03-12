# example rounds pi
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

# Meneruskan Integer setelah ':' akan menyebabkan bidang itu menjadi jumlah minimum karakter yang lebar
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# '!a' diterapkan assii(), '!s' diterapkan str(), '!r' diterapkan repc():
animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')