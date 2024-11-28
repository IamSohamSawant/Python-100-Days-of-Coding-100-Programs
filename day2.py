print("Body mass index calculator")
height=input("Enter your height in m: ")
weight=input("Enter your weight in kg: ")

height_float=float(height)
weight_int=int(weight)

bmi=weight_int/height_float**2
bmi_int=int(bmi)
print(bmi)