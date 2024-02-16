# Write your code here

def last_digit(integer):
    return integer % 10

def remove_last_digit(integer):
    return integer//10

def digit_sum(integer):
    result = 0
    while integer > 0:
        result += last_digit(integer)
        integer = remove_last_digit(integer)
    return result