my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))  # Output: 3
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # Output: 2

my_tuple = (1, 2, 2, 3, 4, 5)

# Using count() to find how many times 2 appears
count_of_2 = my_tuple.count(2)  # Output: 2

# Using index() to find the position of 3
index_of_3 = my_tuple.index(3)  # Output: 3

print("Count of 2:", count_of_2)
print("Index of 3:", index_of_3)
