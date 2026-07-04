"""
Loading and Exploring Data

In real data science projects, you'll work with data stored in files.
This example shows you how to load data from a CSV file and explore it.

What you'll learn:
- How to load data from a CSV file
- How to view basic information about your dataset
- How to display the first/last rows
- How to get summary statistics

Prerequisites: pandas library (install with: pip install pandas)
"""

# Import the pandas library - it's the most popular tool for working with data in Python
# We give it the short name 'pd' so we can type less
import pandas as pd

print("=" * 70)
print("Welcome to Data Loading and Exploration!")
print("=" * 70)
print()

# Step 1: Load data from a CSV file
# CSV stands for "Comma-Separated Values" - a common format for storing data
# We'll use the birds dataset that comes with this repository
print("📂 Loading data from birds.csv...")
print()

# Load the data into a DataFrame (think of it as a smart spreadsheet)
# A DataFrame is pandas' main data structure - it organizes data in rows and columns
data = pd.read_csv('../data/birds.csv')

print("✅ Data loaded successfully!")
print()

# Step 2: Get basic information about the dataset
print("-" * 70)
print("BASIC DATASET INFORMATION")
print("-" * 70)

# How many rows and columns do we have?
num_rows, num_columns = data.shape
print(f"📊 Dataset size: {num_rows} rows × {num_columns} columns")
print()

# What are the column names?
print("📋 Column names:")
for i, column in enumerate(data.columns, 1):
    print(f"   {i}. {column}")
print()

# Step 3: Look at the first few rows of data
# This gives us a quick preview of what the data looks like
print("-" * 70)
print("FIRST 5 ROWS OF DATA (Preview)")
print("-" * 70)
print(data.head())  # head() shows the first 5 rows by default
print()

# Step 4: Look at the last few rows
print("-" * 70)
print("LAST 3 ROWS OF DATA")
print("-" * 70)
print(data.tail(3))  # tail(3) shows the last 3 rows
print()

# Step 5: Get information about data types
print("-" * 70)
print("DATA TYPES AND NON-NULL COUNTS")
print("-" * 70)
print(data.info())  # Shows column names, data types, and count of non-null values
print()

# Step 6: Get statistical summary
print("-" * 70)
print("STATISTICAL SUMMARY (for numerical columns)")
print("-" * 70)
# describe() gives us statistics like mean, std, min, max, etc.
print(data.describe())
print()

# Step 7: Check for missing values
print("-" * 70)
print("MISSING VALUES CHECK")
print("-" * 70)
missing_values = data.isnull().sum()
print("Number of missing values per column:")
print(missing_values)
print()

if missing_values.sum() == 0:
    print("✅ Great! No missing values found.")
else:
    print("⚠️  Some columns have missing values. You may need to handle them.")
print()

# Step 8: Get unique values in a column
print("-" * 70)
print("SAMPLE: UNIQUE VALUES")
print("-" * 70)
# Let's see what unique values exist in the first column
first_column = data.columns[0]
unique_count = data[first_column].nunique()
print(f"The column '{first_column}' has {unique_count} unique value(s)")
print()

# Summary
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print("You've learned how to:")
print("  ✓ Load data from a CSV file using pandas")
print("  ✓ Check the size and shape of your dataset")
print("  ✓ View the first and last rows")
print("  ✓ Understand data types")
print("  ✓ Get statistical summaries")
print("  ✓ Check for missing values")
print()
print("Next step: Try loading other CSV files from the data/ folder!")
print("=" * 70)

# Pro Tips:
# - Always explore your data before analyzing it
# - Check for missing values and understand why they might be missing
# - Look at the data types to ensure they make sense
# - Use head() and tail() to spot any obvious issues with your data
