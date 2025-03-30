def quadratic_roots(a, b, c):
    delta = b**2 - 4*a*c  # Discriminant calculation
    
    if delta > 0:
        root1 = (-b + delta**0.5) / (2 * a)
        root2 = (-b - delta**0.5) / (2 * a)
        return f"Two real roots: {root1}, {root2}"
    elif delta == 0:
        root = -b / (2 * a)
        return f"One real root: {root}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = (abs(delta) ** 0.5) / (2 * a)
        return f"Two complex roots: {real_part} ± {imaginary_part}i"

a, b, c = 1, -3, 2  # Example coefficients for x^2 - 3x + 2 = 0
print(quadratic_roots(a, b, c))