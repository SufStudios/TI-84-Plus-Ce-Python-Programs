import math


def solve_quadratic():
    print("--- Quadratic Equation Solver (ax^2 + bx + c = 0) ---")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    print("\nEq: {}x^2 + {}x + {} = 0".format(a, b, c))
    print("-"*35)

    if a == 0:
        print("Coefficient 'a' cannot be zero.")
        return

    d = b**2 - 4*a*c
    
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print("Roots: {}, {}".format(root1, root2))
        
    elif d == 0:
        root = -b / (2*a)
        print("Root: {}".format(root))
     
    else:
        #Imaginary Numbers
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(d)) / (2*a)
        print("Complex roots:")
        print("{} + {}i".format(real_part, imaginary_part))
        print("{} - {}i".format(real_part, imaginary_part))
    

solve_quadratic()


