"""
Simple Data Analysis

Learn how to analyze data and answer questions about it.
This example demonstrates common data analysis operations.

What you'll learn:
- How to calculate statistics on your data
- How to filter data based on conditions
- How to group and aggregate data
- How to sort data

Prerequisites: pandas library (install with: pip install pandas)
"""

import pandas as pd

print("=" * 70)
print("Simple Data Analysis Tutorial")
print("=" * 70)
print()

# Load a dataset - we'll use the honey production data
print("📂 Loading honey production data...")
data = pd.read_csv('../data/honey.csv')
print("✅ Data loaded!\n")

# Quick look at the data
print("-" * 70)
print("FIRST FEW ROWS")
print("-" * 70)
print(data.head(3))
print()

# SECTION 1: Basic Statistics
print("=" * 70)
print("SECTION 1: CALCULATING STATISTICS")
print("=" * 70)
print()

# Let's look at the 'totalprod' column (total production)
if 'totalprod' in data.columns:
    total_production = data['totalprod']
    
    print("Total Honey Production Statistics:")
    print("-" * 70)
    print(f"  Mean (Average):     {total_production.mean():,.2f}")
    print(f"  Median (Middle):    {total_production.median():,.2f}")
    print(f"  Mode (Most common): {total_production.mode().values[0]:,.2f}")
    print(f"  Std Dev:            {total_production.std():,.2f}")
    print(f"  Minimum:            {total_production.min():,.2f}")
    print(f"  Maximum:            {total_production.max():,.2f}")
    print()

# SECTION 2: Filtering Data
print("=" * 70)
print("SECTION 2: FILTERING DATA")
print("=" * 70)
print()

# Let's filter the data to show only records from a specific year
if 'year' in data.columns:
    year_to_filter = 2000
    filtered_data = data[data['year'] == year_to_filter]
    
    print(f"Showing data for year {year_to_filter}:")
    print("-" * 70)
    print(f"Found {len(filtered_data)} records")
    print()
    print(filtered_data.head())
    print()

# Filter based on multiple conditions
if 'totalprod' in data.columns and 'year' in data.columns:
    # Find records where production was above 10 million pounds after 2010
    high_production = data[(data['totalprod'] > 10000000) & (data['year'] > 2010)]
    
    print("High production years (>10M pounds after 2010):")
    print("-" * 70)
    print(f"Found {len(high_production)} records")
    print()

# SECTION 3: Grouping and Aggregating
print("=" * 70)
print("SECTION 3: GROUPING AND AGGREGATING DATA")
print("=" * 70)
print()

# Group by state and calculate average production
if 'state' in data.columns and 'totalprod' in data.columns:
    # Group the data by state and calculate mean production
    state_averages = data.groupby('state')['totalprod'].mean()
    
    # Sort to see which states have highest average production
    state_averages_sorted = state_averages.sort_values(ascending=False)
    
    print("Top 10 States by Average Honey Production:")
    print("-" * 70)
    for i, (state, avg_prod) in enumerate(state_averages_sorted.head(10).items(), 1):
        print(f"{i:2d}. {state:20s} {avg_prod:,.0f} pounds")
    print()

# SECTION 4: Sorting Data
print("=" * 70)
print("SECTION 4: SORTING DATA")
print("=" * 70)
print()

if 'totalprod' in data.columns:
    # Sort by total production in descending order
    sorted_data = data.sort_values('totalprod', ascending=False)
    
    print("Records with Highest Production:")
    print("-" * 70)
    # Show the top 5 records
    columns_to_show = ['state', 'year', 'totalprod'] if all(col in data.columns for col in ['state', 'year', 'totalprod']) else data.columns[:3]
    print(sorted_data[columns_to_show].head())
    print()

# SECTION 5: Counting Values
print("=" * 70)
print("SECTION 5: COUNTING VALUES")
print("=" * 70)
print()

if 'state' in data.columns:
    # Count how many records we have for each state
    state_counts = data['state'].value_counts()
    
    print("Number of records per state (top 10):")
    print("-" * 70)
    for state, count in state_counts.head(10).items():
        print(f"{state:20s} {count:3d} records")
    print()

# SECTION 6: Answering a Question
print("=" * 70)
print("SECTION 6: ANSWERING A REAL QUESTION")
print("=" * 70)
print()

# Question: Which state had the highest honey production in 2012?
if all(col in data.columns for col in ['state', 'year', 'totalprod']):
    year_2012 = data[data['year'] == 2012]
    
    if len(year_2012) > 0:
        # Find the row with maximum production in 2012
        max_prod_idx = year_2012['totalprod'].idxmax()
        max_prod_state = year_2012.loc[max_prod_idx, 'state']
        max_prod_amount = year_2012.loc[max_prod_idx, 'totalprod']
        
        print("Question: Which state had the highest honey production in 2012?")
        print("-" * 70)
        print(f"Answer: {max_prod_state}")
        print(f"Production: {max_prod_amount:,.0f} pounds")
        print()

# Summary
print("=" * 70)
print("CONGRATULATIONS!")
print("=" * 70)
print("You've learned how to:")
print("  ✓ Calculate basic statistics (mean, median, mode, etc.)")
print("  ✓ Filter data based on conditions")
print("  ✓ Group data and calculate aggregates")
print("  ✓ Sort data to find top/bottom values")
print("  ✓ Count occurrences of values")
print("  ✓ Answer real questions using data")
print()
print("Try this yourself:")
print("  • Find the state with the lowest average production")
print("  • Calculate total production by year")
print("  • Find trends over time")
print("=" * 70)
