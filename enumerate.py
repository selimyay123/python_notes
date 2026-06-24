# The enumerate() function keeps track of the index for an iterable and returns an enumerate object.

languages = ['Spanish', 'English', 'Russian', 'Chinese']

# If we pass the languages list to the enumerate() function and convert its returned value into a list with the list() function, it looks like this:

print(list(enumerate(languages))) # [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

# Each entry in the enumerate object (now a list) is a tuple containing a count, followed by a value from the iterable passed to the enumerate() function.

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

# The enumerate() function also accepts an optional start argument that specifies the starting value for the count. If this argument is omitted, then the count will begin at 0.

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language: {language}')
    # Index 1 and language Spanish
    # Index 2 and language English
    # Index 3 and language Russian
    # Index 4 and language Chinese

    # So far we've only been iterating over one list. But what if you need to iterate over multiple iterables in parallel? Well, you can use the zip() function for that, which combines lists into pairs of elements and returns an iterator of tuples.
    # If we pass a list of developers and ids to the zip() function and convert its returned value into a list with the list() function, here's what it looks like:

    developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
    ids = [1, 2, 3, 4]

    list(zip(developers, ids))
    # [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

    developers1 = ['Naomi', 'Dario', 'Jessica', 'Tom']
    ids1 = [1, 2, 3, 4]

    for name, id in zip(developers1, ids1):
        print(f'Name: {name}')
        print(f'ID: {id}')