# loops are used to repeat a block of code for a set number of times.

programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)

# You can also use a for loop to iterate through other iterables like a string. 

for letter in 'code':
    print(letter)

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

# while loop will repeat a block of code until the condition is False

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')

# Python supports the break and continue statements
# The break statement is used to stop the execution of a loop

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer) # Jess

# The continue statement is used to skip the current iteration of a loop and move onto the next iteration.

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer) # Now the result in the console will be different. The names Jess and Tom are printed because the continue statement skips the second iteration of the loop when developer is equal to Naomi, and does not print that name to the console.

# Both for and while loops can be combined with an else clause, which is executed only when the loop is not terminated by a break statement. 

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
        else:
            print(f"'{word}' has no vowels")

# The range() function is used to generate a sequence of integers. 
# range(start, stop, step)
# The required stop argument is an integer that represents the end point for the sequence of numbers being generated.

for num in range(3):
    print(num) # 0 1 2

# If a start argument is not specified, then the default is 0. Otherwise, you can use the optional start argument to start the sequence of integers at a integer other than 0. Here is an example of generating a sequence of integers between 1 and 4:

for num1 in range(1, 5):
    print(num1) # 1 2 3 4 

for num3 in range(2, 11, 2):
    print(num3) # 2 4 6 8 10

# If you want to generate a sequence of integers in decrementing order, then you can use a negative integer for the step argument, like this:

for num4 in range(40, 0, -10):
    print(num4) # 40 30 20 10