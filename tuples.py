# Tuples are similar to lists, but while lists are a mutable data type, tuples are immutable. This means that the elements in a tuple cannot be changed once it's created.

developer = ('selim', 25, 'AI Engineer')
print(developer[1]) # 25
developer_name = 'selim'
print(tuple(developer_name)) # ('s', 'e', 'l', 'i', 'm')

programming_languages = ('Python', 'Java', 'C++', 'Rust')
'Rust' in programming_languages # True
'JavaScript' in programming_languages # False

desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3] # ('pie', 'cookies')

developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer
print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

# count(): This method is used to determine how many times an item appears in a tuple.

programming_languages1 = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages1.count('Rust')) # 2

# index(): This method is used to find the index where a particular item is present in a tuple. 

print(programming_languages1.index('Java')) # 1

numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]
# The sorted() function will always create a new list of the sorted values. This differs from the sort() method which sorts the elements of a list in place and does not return a new list.

