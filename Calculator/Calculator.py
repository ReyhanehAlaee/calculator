import math

sin = math.sin
cos = math.cos
tan = math.tan
fac = math.factorial
sqrt = math.sqrt

a = int(input("Enter a: "))
b = int(input("Enter b: "))
op = input("Enter op(+, -, *, /, sin, cos, tan, cot, factorial, sqrt): ")

if op == "+":
    r = a + b
if op == "-":
    r = a - b
if op == "*":
    r = a * b
if op == "/": 
    if b == 0:
        r = "error"
    else:
        r = a / b
if op == "sin":
    r = sin(a)

if op == "cos":
    r = cos(a)

if op == "tan":
    r = tan(a)

if op == "cot":
    z= tan(a)
    r = 1/z

if op == "fac":
    if a<0:
        r = "error"
    else:
        r = fac(a)

if op == "sqrt":
    r = sqrt(a)

print (r)


