# def square_of_list(ilist):
#     olist = []

#     for element in ilist:
#         olist.append(element ** 2)

#     return olist

# def square_of_list(ilist):
#     return [el ** 2 for el in ilist]

# first level citizens
# square_of_list = lambda ilist: [el ** 2 for el in ilist]

# second order functions
def gen_list_transformer(transformation):
    def transformer(ilist):
        return [transformation(el) for el in ilist]
    return transformer


square_of_list = gen_list_transformer(lambda n: n ** 2)
cube_of_list = gen_list_transformer(lambda n: n ** 3)

print(square_of_list([1, 2, 3, 4, 5]))
print(cube_of_list([1, 2, 3, 4, 5]))

