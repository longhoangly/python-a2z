import itertools

print(list(itertools.product("ABC", "DE", [1, 2, 3])))
print(list(itertools.product([1, 2, 3], [4, 5], [7, 8, 9])))

print(list(itertools.permutations("ABC", 3)))
print(list(itertools.permutations([1, 2, 3], 3)))

print(list(itertools.combinations("ABC", 3)))
print(list(itertools.combinations([1, 2, 3], 3)))

print(list(itertools.combinations_with_replacement("ABC", 3)))
print(list(itertools.combinations_with_replacement([1, 2, 3], 3)))
