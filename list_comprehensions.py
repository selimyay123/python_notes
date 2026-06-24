# List comprehension allows you to create a new list in a single line by combining a loop and condition directly within square brackets. This makes the code shorter and often easier to read.

even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)

# n this refactored example, the even_numbers list is created using a single line of code. The list comprehension loops through numbers from 0 to 20, and includes only those that are divisible by 2. This approach is more compact and eliminates the need for a separate loop and conditional block.

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

# Another way to create a list starting from an existing iterable is the filter() function.
# The filter() function is used to select elements from an iterable that meet a specific condition. 
# The filter() function is used to select elements from an iterable that meet a specific condition. The filter() function accepts a function and an iterable for its arguments. In this example, we are passing in an is_long_word function into the filter() function to check if the current word count is greater than 4. All words that have a character count greater than 4 are added into a new list and assigned to the long_words variable.

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']

# Aside from the filter() function, there are a few more functions that are helpful when working with lists. Another function to be aware of is the map() function, which takes an iterable and applies a function to each of its elements. Here is an example of using the map() function to convert a list of temperatures from Celsius to Fahrenheit:

# Just like the filter() function, map() accepts a function and an iterable for its arguments. The to_fahrenheit function takes a temperature and converts it from Celsius to Fahrenheit.


celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))

# The last function we will look at is the sum() function. This function is used to get the sum from an iterable like a list or tuple.

numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # 50