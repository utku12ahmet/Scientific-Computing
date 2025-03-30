import math

def calculate_euler(n_terms=20):
    e_approximation = sum(1 / math.factorial(i) for i in range(n_terms))
    return e_approximation

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_euler_2(n_terms=20):
    e_approximation = sum(1 / factorial(i) for i in range(n_terms))
    return e_approximation
# Usage
e_value = calculate_euler_2(20)
print(f"Approximate value of Euler's number: {e_value}")