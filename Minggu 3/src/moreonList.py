fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple')) # Hasilnya 2. Karena apple muncul 2 kali

fruits.count('tangerine') # Hasilnya 0. Karena tidak ada di List fruits

fruits.index('banana') # Hasilnya 3. Karena index dari urutan 0

fruits.index('banana', 4) # Find next banana starting a position 4

fruits.reverse()
print(fruits) #['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append('grape')
print(fruits) #['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()
print(fruits) #['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

fruits.pop()
print(fruits) #['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']