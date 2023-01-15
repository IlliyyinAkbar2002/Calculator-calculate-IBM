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
# condition 
result = int(formula)
if result <= 18:
    print("Your BMI 18, is you are underweight.")
elif result <= 24:
    print("Your BMI is 23, you have a normal weight.")
elif result <= 27:
    print("Your BMI is 26, you are slightly overweight.")
elif result <= 30:
    print("Your BMI is 29, you are slightly overweight.")
elif result >= 30:
    print("Your BMI is 33, you are obese.")
elif result >= 40:
    print("Your BMI is 40, you are clinically obese.")

