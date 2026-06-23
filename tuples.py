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