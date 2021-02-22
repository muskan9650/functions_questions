#Write a Python program that accepts a hyphen-separated sequence of words as input and 
#prints the words in a hyphen-separated sequence after sorting them alphabetically.
#green-red-black-white 
items="green-red-black-white"
item= items.split('-')
items.sort()
print('-'.join(items))