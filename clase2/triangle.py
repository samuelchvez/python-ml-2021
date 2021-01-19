triangle = lambda n: '\n'.join([
    f"{' ' * (n - 1 - i)}{'*' * (2 * i + 1)}"
    for i in range(n)
])



print(triangle(3))
print('')
print(triangle(5))
