# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    result = max(num1, num2, num3)
    return result

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    result = min(num1, num2, num3)
    return result

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number > 0:
        number = "Positive"
        return number
    
    elif number == 0:
        number = "Zero"
        return number
    
    elif number < 0:
        number = "Negative"
        return number

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    result = "*"

    for i in range(rows + 1):
        if i >= 2:
            result += ("\n" + (i * "*"))    # .strip removes space on both sides while .rstrip removes spaces on one side
            i += 1

        if i == rows + 1:
            return result


# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    numbers = range(1, limit + 1)
    numbers = list(numbers)     # puts into a list to then convert to a string
    i = 0       # start of count

    while i < len(numbers):
        if numbers[i] % 3 == 0:
            numbers[i] = "Multiple of 3"
        i += 1

        if i == len(numbers):
            result = '\n'.join(map(str, numbers))
            return(result)

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    numbers = range(start, end + 1)
    even = [number for number in numbers if number % 2 == 0]    # Puts only even numbers
    result = sum(even)
    return result