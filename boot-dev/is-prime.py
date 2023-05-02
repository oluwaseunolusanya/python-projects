'''PRIME

A math student is working on a project and needs an easy way to determine whether or not a number is prime. She asked you to write a program to help her.
Challenge

Write a function that takes a single number as input and returns True if it is a prime number or False if it is not.
What is a prime number?

A prime number is a number that is only divisible by itself and 1. For example, 2, 3, 5, and 7 are all prime numbers, but 4, 6, 8, and 9 are not.'''
def is_prime(number):
    remainder_count = 0
    for divisor in range(1, number + 1):
        remainder = number % divisor
       # print(f"{number} % {divisor} is {remainder}.")
       # print(remainder)
        if remainder == 0:
            remainder_count += 1
        # print(remainder_count)
    return remainder_count == 2

# Test Suite
for i in range(1, 25):
    print(f"{i} is prime: {is_prime(i)}")