import openpyxl as px

# Load the Excel file to analyze its structure
file_path = '"C:\Users\Mark Cedrick\Documents\Kuya Mark\Business Intelligence Class Fall 2024\Module 7 Creating Quality Vizualization\Module 7 Creating Quality Vizualization Assignment.xlsx"'
workbook = px.load_workbook(file_path)

# Get sheet names to understand the structure
sheet_names = workbook.sheetnames
sheet_names
