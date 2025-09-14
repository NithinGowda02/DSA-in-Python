#generate squares of numbers 1 to 20

squares = [x ** 2 for x in range(1,21)]
print(squares)

# extract even numbers from 1 to 20

even_num = [x for x in range(1, 21) if x%2 == 0]
print(even_num)