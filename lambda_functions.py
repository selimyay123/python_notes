# Throughout the previous lessons, you have been used to defining functions by using the def keyword like this:

def square(num):
    return num ** 2

print(square(4)) # 16

# But when it comes to working with high order functions like map() and filter(), you can use an anonymous inline function. This is where lambda functions come in.

# Here's what the square() function looks like when refactored into a lambda function:

lambda num: num ** 2

# As mentioned earlier, lambda functions are anonymous, so this function no longer has the name square associated with it. Lambda functions are great when you need to use them in higher order functions like this:

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))