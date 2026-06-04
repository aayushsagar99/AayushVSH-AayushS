import sympy as sp
def process_complex_equation():
                print("--- Equation Processor ---")
                print("Rules: Use parentheses for functions: sin(x), cos(x), log(x), sqrt(x)")
                print("sqrt=spuare root")
                print("log=logarithm")
                print("sin=sine")
                print("cos=cosine")
                print("tan=tangent")
                print("exp=exponential")
                print("ln=natural logarithm")
                print("cbrt=cube root")
                import math
                print(f"pi={math.pi}")
                print(f"e={math.e}")
                print("Example inputs: sin(x) = 0.5  OR  cos(x)**2 + log(x)")
                print("-"*85)
                
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

if __name__ == "__main__": process_complex_equation()
