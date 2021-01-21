

# def factorial(n):
#     result = 1

#     for i in range(2, n + 1):
#         result *= i

#     return result


from functools import reduce


factorial = lambda n: reduce(
    lambda acc, val: acc * val,
    range(2, n + 1),
    1
)


print(factorial(6))
print(factorial(10))
print(factorial(-10))