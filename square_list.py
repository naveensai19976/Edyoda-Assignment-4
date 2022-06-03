def square_numbers(n):
  return n * n
numbers = [4, 5, 2, 9]
print("Original List: ",numbers)
result = map(square_numbers, numbers)
print("Square the elements of the list using map():")
print(list(result))