a = float(input("Enter length of Side A: "))
b = float(input("Enter length of Side B: "))
c = float(input("Enter length of Side C: "))
if (a + b <= c) or (a + c <= b) or (b + c <= a) or (a <= 0 or b <= 0 or c <= 0):
    print("Not a Triangle")
else:
    sides = sorted([a, b, c])
    x = sides[0]
    y = sides[1]
    z = sides[2]
if(x**2 + y**2, 2) == (z**2, 2):
        print("Right-angled Triangle")
elif a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
     print("Scalene Triangle")
    