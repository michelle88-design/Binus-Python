import math 
a = float(input("Enter Value A:"))
b = float(input("Enter Value B:"))
c = float(input("Enter Value C:"))
if a == 0:
    print("It is not a quadratic equation")
else:
    equation = str(a) + "x^2" + str(b) + "x" + str(c) + "= 0"
    d = (b**2) - (4*a*c)
    print(d)
if d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print("It has distinct roots")
    print("Quadratic Equation:" + str(equation))
    print("discriminant value" + str(d))
    print("Root x1:" + str(x1))
    print("Root x2:" + str(x2))
elif(d == 0):
    x = -b/(2*a)
    print("It has a double root")
    print("Quadratic Equation" + str(equation))
    print("discriminant value" + str(d))
    print("root value" + str(x))
else:
    real = -b/(2*a)
    imaginary = math.sqrt(-d)/(2*a)
    print("It has imaginary root")
    print("Quadratic Equation:" + str(equation))
    print("discriminant value" + str(d))
    print("Formula for x1:" + str(real + imaginary) + "i")
    print("Formula for x1:" + str(real - imaginary) + "i")
    