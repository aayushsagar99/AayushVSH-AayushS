import math
import time
print("WELCOME!!! Pick whatever math problem to solve!")
main=int(input("Enter 1 for simple, enter 2 for complex or enter 3 to exit: "))
if main==3:
    print("bye!")
    time.sleep(1)
    exit()
chances=3
if (main>3):
    print("Enter only 1, 2, or 3!")
    chances=chances-1
    if chances==1:
        print(chances," chance left!")
    else:
        print(chances," chances left!")
while main!=3:
    if main==1:
        print("simple")
        h=int(input("Enter 1 for addition, enter 2 for subtraction, enter 3 for multiplication, enter 4 for divition, or enter 5 to exit:"))
        if h==1:
            print("addition")
            time.sleep(1)
            ad=float(input("What is the first number to add: "))
            ad2=float(input("What is the second number to add: "))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{ad}+{ad2}={ad+ad2}")
        elif h==2:
            print("subtraction")
            time.sleep(1)
            su=float(input("What is the first number to subtract: "))
            su2=float(input("What is the second number to subtract: "))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{su}-{su2}={su-su2}")
        elif h==3:
            print("multiplication")
            time.sleep(1)
            mu=float(input("What is the first number to multiply: "))
            mu2=float(input("What is the second number to multiply: "))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{mu}*{mu2}={mu*mu2}")
        elif h==4:
            print("division")
            time.sleep(1)
            di=float(input("What is the first number to divide: "))
            di2=float(input("What is the second number to divide: "))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{di}/{di2}={di*di2}")
        elif h==5:
            print("bye!")
            time.sleep(1)
            exit()
    elif main==2:
        print("complex")
        j=int(input("Enter 1 for square root, enter 2 for cube root, enter 3 for circumfirence of a circle, enter 4 for powers, enter 5 for factorial, enter 6 for sin, enter 7 for cos, enter 8 for tan, enter 9 for hyp, enter 10 to create, or enter 11 to exit:"))
        if j==1:
            print("square root")
            time.sleep(1)
            sq=float(input("Which number should be square rooted:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"The square root of {sq} is {math.sqrt(sq)}")
            time.sleep(1)
        elif j==2:
            print("cube root")
            time.sleep(1)
            cb=float(input("Which number should be cube rooted:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"The square root of {cb} is {math.cbrt(cb)}")
            time.sleep(1)
        elif j==3:
            print("circumfirence")
            time.sleep(1)
            print(f"NOTE: The value of pi is {math.pi} | pi={math.pi}")
            d=float(input("What is the diameter:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"The circumfrence of the circle is {math.pi*d}")
            time.sleep(1)
        elif j==4:
            print("powers")
            time.sleep(1)
            ba=float(input("What is the base number:"))
            ex=int(input("What is the exponential number:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{ba}^{ex}={math.pow(ba, ex)}")
            time.sleep(1)
        elif j==5:
            print("factorial")
            time.sleep(1)
            fa=int(input("What is the factorial number:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"{fa} factorial is {math.factorial(fa)}")
            time.sleep(1)
        elif j==6:
            print("sin")
            time.sleep(1)
            sin=float(input("What is the sin number:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"The sin of {sin} is {math.sin(sin)}")
            time.sleep(1)
        elif j==7:
            print("cos")
            time.sleep(1)
            cos=float(input("What is the cos number:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"The cos of {cos} is {math.cos(cos)}")
        elif j==8:
            print("tan")
            time.sleep(1)
            tan=float(input("What is the tan number:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"The tan of {tan} is {math.tan(tan)}")
            time.sleep(1)
        elif j==9:
            print("hypotenuse")
            time.sleep(1)
            hyp=float(input("What is the first hypotenuse number:"))
            hyp2=float(input("What is the second hypotenuse number:"))
            print("Thinking...")
            time.sleep(2.5)
            print(f"The hypotenuse of {hyp} and {hyp2} is {math.hypot(hyp, hyp2)}")
            time.sleep(1)
        elif j==10:
            print("create")
            time.sleep(1)
            import sympy as sp
            def process_complex_equation():
                print("--- Equation Processor ---")
                print("Rules: Use parentheses for functions: sin(x), cos(x), log(x), sqrt(x)")
                print("Example inputs: sin(x) = 0.5  OR  cos(x)**2 + log(x)")
                print("-----------------------------------")
                
                user_input = input("Enter expression or equation: ")
                x = sp.Symbol('x')
                
                try:
                    # Check if the user entered an equation with an '=' sign
                    if "=" in user_input:
                        left_side, right_side = user_input.split("=")
                        # Parse both sides and build a SymPy Equation object
                        equation = sp.Eq(sp.sympify(left_side.strip()), sp.sympify(right_side.strip()))
                        print(f"\nParsed Equation: {equation}")
                        
                        # Solve the equation for x
                        solutions = sp.solve(equation, x)
                        print(f"Solutions for x: {solutions}")
                        
                    else:
                        # Handle plain expressions (no equals sign)
                        expression = sp.sympify(user_input)
                        print(f"\nParsed Expression: f(x) = {expression}")
                        print(f"Derivative: {sp.diff(expression, x)}")
                        print(f"Integral: {sp.integrate(expression, x)}")

                except Exception as e:
                    print(f"\nSyntax Error: Make sure to use explicit syntax like 'sin(x)' instead of 'sin x'.")
                    print(f"Details: {e}")

            if __name__ == "__main__":
                process_complex_equation()

        elif j==11:
            print("bye!")
            time.sleep(1)
            break
        elif (j>11):
            print("Enter only 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, or 11!")
            chances=chances-1
            if chances==1:
                print(chances," chance left!")
            else:
                print(chances," chances left!")
    elif chances==0:
        print("bye!")
        time.sleep(1)
        break