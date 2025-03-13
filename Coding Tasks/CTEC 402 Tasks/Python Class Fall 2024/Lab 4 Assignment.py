import re
import numpy as np

def validate_phone_number(phone):
    """Validate phone number in the format XXX-XXX-XXXX."""
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return re.match(pattern, phone)

def validate_zip_code(zipcode):
    """Validate ZIP code in the format XXXXX-XXXX."""
    pattern = r"^\d{5}-\d{4}$"
    return re.match(pattern, zipcode)

def get_matrix_input(prompt):
    """Get a 3x3 matrix from user input, validating for numeric values."""
    matrix = []
    print(prompt)
    for i in range(3):
        while True:
            row = input(f"Enter row {i+1} (3 numbers separated by space): ").split()
            if len(row) == 3 and all(element.replace('.', '', 1).isdigit() for element in row):
                matrix.append([float(num) for num in row])
                break
            else:
                print("Invalid input. Please enter three numbers separated by spaces.")
    print("Your matrix is:")
    print(np.array(matrix))
    return np.array(matrix)

def display_results(result_matrix):
    """Display results, transpose, row means, and column means with 2 decimal places."""
    # Formatting the result matrix with 2 decimal places
    formatted_result = np.round(result_matrix, 2)
    formatted_transpose = np.round(result_matrix.T, 2)
    row_means = np.round(np.mean(result_matrix, axis=1), 2)
    column_means = np.round(np.mean(result_matrix, axis=0), 2)

    print("The results are:")
    print(formatted_result)
    print("\nThe Transpose is:")
    print(formatted_transpose)
    print("\nThe row and column mean values of the results are:")
    print("Row:", row_means)
    print("Column:", column_means)

def matrix_operations():
    """Main function to execute matrix operations."""
    print("***************** Welcome to the Python Matrix Application ***********")
    while True:
        play = input("Do you want to play the Matrix Game?\nEnter Y for Yes or N for No: ").upper()
        if play == 'N':
            print("*********** Thanks for playing Python Numpy ***************")
            break
        elif play != 'Y':
            print("Invalid choice. Please enter Y or N.")
            continue

        # Get and validate phone number
        phone = input("Enter your phone number (XXX-XXX-XXXX): ")
        while not validate_phone_number(phone):
            phone = input("Your phone number is not in correct format. Please re-enter: ")

        # Get and validate ZIP code
        zipcode = input("Enter your zip code+4 (XXXXX-XXXX): ")
        while not validate_zip_code(zipcode):
            zipcode = input("Your zip code is not in correct format. Please re-enter: ")

        # Enter and display matrices
        matrix1 = get_matrix_input("Enter your first 3x3 matrix:")
        matrix2 = get_matrix_input("Enter your second 3x3 matrix:")

        # Matrix operation selection
        print("\nSelect a Matrix Operation from the list below:")
        print(" a. Addition\n b. Subtraction\n c. Matrix Multiplication\n d. Element by element multiplication")
        choice = input("Enter your choice (a/b/c/d): ").lower()

        if choice == 'a':
            result = matrix1 + matrix2
            print("\nYou selected Addition.")
        elif choice == 'b':
            result = matrix1 - matrix2
            print("\nYou selected Subtraction.")
        elif choice == 'c':
            result = np.matmul(matrix1, matrix2)
            print("\nYou selected Matrix Multiplication.")
        elif choice == 'd':
            result = matrix1 * matrix2
            print("\nYou selected Element by element multiplication.")
        else:
            print("Invalid selection. Try again.")
            continue

        # Display results and continue
        display_results(result)

# Run the application
if __name__ == "__main__":
    matrix_operations()
