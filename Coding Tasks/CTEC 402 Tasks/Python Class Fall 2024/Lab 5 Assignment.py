import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_file(file_path):
    """Load a CSV file and return the data as a DataFrame."""
    try:
        data = pd.read_csv(file_path)
        print(f"\nFile '{file_path}' loaded successfully.")
        return data
    except FileNotFoundError:
        print("\nError: File not found. Please check the file path.")
        return None


def analyze_column(data, column_name):
    """Analyze a selected column and display statistics and a histogram."""
    try:
        column = data[column_name].dropna()  # Drop NaN values for accurate analysis
        print(f"\nThe statistics for the column '{column_name}' are:")
        print(f"Count = {column.count()}")
        print(f"Mean = {column.mean():.2f}")
        print(f"Standard Deviation = {column.std():.2f}")
        print(f"Min = {column.min()}")
        print(f"Max = {column.max()}")

        # Display histogram
        plt.hist(column, bins=20, edgecolor='black')
        plt.title(f"Histogram of {column_name}")
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        plt.grid(axis='y', alpha=0.75)
        plt.show()
    except KeyError:
        print("\nError: Column not found. Please select a valid column.")


def main():
    """Main function to drive the Python Data Analysis App."""
    print("***************** Welcome to the Python Data Analysis App **********")

    while True:
        print("\nSelect the file you want to analyze:")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program")

        file_choice = input("Enter your choice (1/2/3): ").strip()

        if file_choice == "1":
            file_path = r"C:\Users\Nabila Majio\Documents\Nabila Majio\Python Class Fall 2024\Lab 5 Documents\PopChange.csv"
            data = load_file(file_path)
            if data is not None:
                print("\nYou have entered Population Data.")
                columns = ["Pop Apr 1", "Pop Jul 1", "Change Pop"]
        elif file_choice == "2":
            file_path = r"C:\Users\Nabila Majio\Documents\Nabila Majio\Python Class Fall 2024\Lab 5 Documents\Housing.csv"
            data = load_file(file_path)
            if data is not None:
                print("\nYou have entered Housing Data.")
                columns = ["AGE", "BEDRMS", "BUILT", "ROOMS", "UTILITY"]
        elif file_choice == "3":
            print("\n*************** Thanks for using the Data Analysis App **********")
            break
        else:
            print("\nInvalid input. Please select a valid option.")
            continue

        if data is not None:
            while True:
                print("\nSelect the column you want to analyze:")
                for i, col in enumerate(columns, start=1):
                    print(f"{chr(96 + i)}. {col}")
                print(f"{chr(96 + len(columns) + 1)}. Exit Column")

                col_choice = input("Enter your choice: ").strip()

                if col_choice in [chr(96 + i) for i in range(1, len(columns) + 1)]:
                    selected_col = columns[ord(col_choice) - 97]
                    print(f"\nYou selected {selected_col}")
                    analyze_column(data, selected_col)
                elif col_choice == chr(96 + len(columns) + 1):
                    print("\nYou selected to exit the column menu.")
                    break
                else:
                    print("\nInvalid input. Please select a valid option.")


if __name__ == "__main__":
    main()
