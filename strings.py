# String slicing lets you extract a portion of a string or work with only a specific part of it.
# string[start:stop]

my_str = 'hello world'
print(my_str[1:4]) # ell

# You can also omit the start and stop indices, and Python will default to 0 or the end of the string, respectively.

print(my_str[:4])
print(my_str[4:])

# upper(): Returns a new string with all characters converted to uppercase.

my_str1 = 'hello world'
print(my_str.upper())

# lower(): Returns a new string with all characters converted to lowercase.

my_str2 = 'HELLO'
print(my_str2.lower()) 

# strip(): Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.

my_str3 = '  hello  '
print(my_str3.strip())

# replace(old, new): Returns a new string with all occurrences of old replaced by new.

my_str4 = 'hello world'
print(my_str.replace('hello', 'hi'))

# split(separator): Splits a string on a specified separator into a list of strings. If no separator is specified, it splits on whitespace.

my_str5 = 'hello world'
print(my_str5.split()) # ['hello', 'world']

# join(iterable): Joins elements of an iterable into a string with a separator.

my_list = ['hello', 'world']
joined_str = ' '.join(my_list)
print(joined_str)

# startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.

my_str6 = 'hello world'
print(my_str.startswith('hello'))

# endswith(suffix)

print(my_str6.endswith('world'))

# find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.

print(my_str6.find('world'))

# count(substring): Returns the number of times a substring appears in a string.

print(my_str6.count('o'))

# capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.

print(my_str6.capitalize())

# isupper(): Returns True if all letters in the string are uppercase and False if not.

print(my_str6.isupper())

# islower(): Returns True if all letters in the string are lowercase and False if not.

print(my_str6.islower())

# title(): Returns a new string with the first letter of each word capitalized.

print(my_str6.title())