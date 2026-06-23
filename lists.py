cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[0]) # Los Angeles
print(cities[-1]) # Tokyo

# The list() constructor is used to convert an iterable into a list like this:

developer = 'selim'
print(list(developer)) # ['s', 'e', 'l', 'i', 'm']

# To get the total number of elements in a list, you can use the len() function like this:

print(len(cities)) # 3

cities[0] = 'Istanbul'
print(cities) # ['Istanbul', 'London', 'Tokyo']

# If you want to remove an element from a list you can use the del keyword like this:

del cities[1]
print(cities) # ['Istanbul', 'Tokyo']

# Sometimes it is helpful to check if an element is inside the list. To do that, you can use the in keyword like this:

print('Istanbul' in cities) # True

developer1 = ['selim', 25, ['Python', 'Flutter', 'Next.js']]
print(developer1[2][1])

# Unpacking values from a list is a technique used to assign values from a list to new variables.

developer2 = ['selim', 25, 'AI Engineer']
name, age, job = developer2
print(name, age, job)

# Similar to strings, you can access portions of a list by using the slice operator like this:

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:3])

# common list methods

# append()
# This is used to add an item to the end of the list.
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)

# If you want to add one list at the end of another, you can also use the append() method like this:

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers1.append(numbers2) 
print(numbers1) # [1, 2, 3, [4, 5, 6]]
# But if you want to add all of the individual numbers from the numbers2 list at the end of the numbers list, then you can use the extend() method.
numbers1.extend(numbers2)
print(numbers1) # [1, 2, 3, 4, 5, 6]

# To insert an element at a specific index in a list, you can use the insert() method.

numbers.insert(2, 2.5)
print(numbers) # [1, 2, 2.5, 3, 4, 5]

# If you want to remove an element from a list, you can use the remove() method. The remove()

numbers.remove(1)
print(numbers) # [2, 2.5, 3, 4, 5] 
# It is important to note that this method will only remove the first occurrence of an item. Not all of them:

# To remove an element at a specific index in the list, you can use the pop() method like this:

numbers3 = [1, 2, 3, 4]
popped = numbers3.pop(2)
print(popped) # 3
print(numbers3) # [1, 2, 4]
# If you don't specify an element for the pop method, then the last element is removed.

# If you need to empty the list, then you can use the clear() method like this:
numbers3.clear()
print(numbers3) # []

# The next method we will take a look at is the sort() method. This method is used to sort the elements in place. Here is an example of sorting a random list of numbers in place:

numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()
print(numbers) # [1, 2, 19, 35, 41, 67]

# In contrast to the sort() method, there is the sorted() function which works for any iterable and returns a new sorted list instead of modifying the original list. For example:

numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)
print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]

# The next method we will take a look at is the reverse() method. This method, will reverse a list of elements in place like this:

numbers4 = [1, 2, 3, 4]
numbers4.reverse()
print(numbers4) # [4, 3, 2, 1] 

# The last method we will take a look at is the index method. This is used to find the first index where an element can be found in a list. 

programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1