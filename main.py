height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# print(type(height + weight))

# Convert string to floating point number
first = float(height)
second = float(weight)

# Fourmula IBM
formula = second / first ** 2

# convert float to integer
# print(type(formula))
result = int(formula)

# Print calculate height and weight IBM formula
print(result)

