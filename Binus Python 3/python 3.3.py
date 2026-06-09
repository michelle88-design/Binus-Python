print("Temperature Conversion Menu")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")
choice = int(input("choose option 1-6: "))
if(choice in (1,2,3,4,5,6)):
    temp = float(input("enter temperature: "))
if(choice == 1):
    print(str((temp*9/5)+32) + "°F") 
elif(choice == 2):
    print(str(temp+273) + "K")
elif(choice == 3):
    print(str((temp-32)*5/9) + "°C")
elif(choice == 4): 
    print(str((temp-32)*5/9)+273 + "K")
elif(choice == 5):
    print(str(temp-273) + "K")
elif(choice == 6):
    print((str((temp-273)*9/5)+32) + "°F")
