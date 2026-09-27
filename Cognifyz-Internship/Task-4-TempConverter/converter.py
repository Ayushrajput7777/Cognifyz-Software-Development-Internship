# Task 4: Temp Converter
temp = float(input("Temp dalo: "))
unit = input("Unit C ya F? : ").upper()

if unit == 'C':
    print(f"{temp}C = {(temp*9/5)+32}F")
else:
    print(f"{temp}F = {(temp-32)*5/9}C")