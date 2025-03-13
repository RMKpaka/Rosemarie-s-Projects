def compute_factorial(n):
    """Computes the factorial of a given non-negative integer n."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

while True:
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            print(f"Factorial of {num} is {compute_factorial(num)}")
            break
    except ValueError:
        print("Error: Invalid input. Please enter a valid non-negative integer.")
