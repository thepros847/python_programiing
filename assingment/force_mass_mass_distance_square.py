gravity = Constant
initial_mass = float(input("Enter a number: "))
final_mass = float(input("Enter a number: "))
distance = float(input("Enter a number: "))
force = gravity * initial_mass * final_mass / distance * distance
print("The output force is:",force) 