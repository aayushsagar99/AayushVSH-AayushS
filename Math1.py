import sympy
# Substitute values into the force formula
result = force.subs({M: 10, a: 9.8})
print(f"Numerical Force: {result}")
# Output: Numerical Force: 98.0

M, a, t, h = sympy.symbols('M a t h')

# 1. Area of a triangle (using h for height and a for base)
area_triangle = 0.5 * a * h

# 2. Physics: Momentum (M often used for mass in non-standard or 'm', a for acceleration)
# Force = mass * acceleration
force = M * a

# 3. Kinematics: Displacement (a = acceleration, t = time)
# s = ut + 0.5 * a * t^2 (assuming u=0)
displacement = 0.5 * a * t**2

# 4. Enthalpy (H), Temperature (T), Mass (M)
# Heat transfer Q = M * c * deltaT (if M is mass)

print(f"Area: {area_triangle}")
print(f"Force: {force}")
print(f"Displacement: {displacement}")
