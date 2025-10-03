"""
Real World Example: Complete Data Science Workflow

This example ties everything together, showing you a complete data science project
from start to finish. We'll analyze bird strike data to answer real questions.

What you'll learn:
- How to approach a data science problem
- Complete workflow: Load → Clean → Analyze → Visualize → Conclude
- How to handle real-world data issues
- How to draw meaningful conclusions

Prerequisites: 
- pandas library (install with: pip install pandas)
- matplotlib library (install with: pip install matplotlib)

Real-world context:
Bird strikes (when birds collide with aircraft) are a safety concern for aviation.
Let's analyze bird strike data to understand patterns and risks.
"""

import pandas as pd
import matplotlib.pyplot as plt

print("=" * 80)
print("REAL WORLD DATA SCIENCE PROJECT: BIRD STRIKE ANALYSIS")
print("=" * 80)
print()

# STEP 1: DEFINE THE PROBLEM
print("=" * 80)
print("STEP 1: DEFINE THE PROBLEM")
print("=" * 80)
print()
print("Questions we want to answer:")
print("  1. How many bird strikes occur?")
print("  2. When do bird strikes most commonly occur?")
print("  3. What are the most common bird species involved?")
print("  4. What is the typical damage level?")
print()
input("Press Enter to continue...")
print()

# STEP 2: LOAD THE DATA
print("=" * 80)
print("STEP 2: LOAD THE DATA")
print("=" * 80)
print()
print("📂 Loading bird strike data...")

try:
    data = pd.read_csv('../data/birds.csv')
    print(f"✅ Successfully loaded {len(data)} records")
    print()
except FileNotFoundError:
    print("❌ Error: birds.csv not found in data/ folder")
    print("Please make sure the data file exists.")
    exit(1)

# STEP 3: EXPLORE THE DATA
print("=" * 80)
print("STEP 3: EXPLORE THE DATA")
print("=" * 80)
print()

print("Dataset Information:")
print("-" * 80)
print(f"  • Shape: {data.shape[0]} rows × {data.shape[1]} columns")
print(f"  • Columns: {', '.join(data.columns.tolist())}")
print()

print("First few rows:")
print("-" * 80)
print(data.head(3))
print()

print("Data types:")
print("-" * 80)
print(data.dtypes)
print()

# STEP 4: CLEAN THE DATA
print("=" * 80)
print("STEP 4: CLEAN THE DATA")
print("=" * 80)
print()

# Check for missing values
print("Checking for missing values...")
missing_counts = data.isnull().sum()
missing_percentage = (missing_counts / len(data)) * 100

print("-" * 80)
for column in data.columns:
    if missing_counts[column] > 0:
        print(f"  • {column}: {missing_counts[column]} missing ({missing_percentage[column]:.1f}%)")

if missing_counts.sum() == 0:
    print("  ✅ No missing values found!")
print()

# Handle missing values in a specific column if needed
# For this example, we'll work with the data as-is, but in real projects
# you might need to fill or remove missing values

print("Data cleaning notes:")
print("-" * 80)
print("  • In a real project, you would:")
print("    - Decide how to handle missing values (remove, fill, or keep)")
print("    - Check for duplicate records")
print("    - Validate data types")
print("    - Look for outliers or incorrect values")
print("  • For this example, we'll proceed with the data as-is")
print()

# STEP 5: ANALYZE THE DATA
print("=" * 80)
print("STEP 5: ANALYZE THE DATA")
print("=" * 80)
print()

# Analysis 1: Total number of incidents
total_strikes = len(data)
print("Analysis 1: Overview")
print("-" * 80)
print(f"  • Total bird strikes recorded: {total_strikes:,}")
print()

# Analysis 2: Find the most common bird species
if 'Bird Species' in data.columns:
    print("Analysis 2: Most Common Bird Species")
    print("-" * 80)
    top_species = data['Bird Species'].value_counts().head(5)
    for i, (species, count) in enumerate(top_species.items(), 1):
        print(f"  {i}. {species}: {count} strikes ({count/total_strikes*100:.1f}%)")
    print()

# Analysis 3: Analyze by time (if time column exists)
time_column = None
for col in ['FlightDate', 'Date', 'Time']:
    if col in data.columns:
        time_column = col
        break

if time_column:
    print(f"Analysis 3: Temporal Analysis")
    print("-" * 80)
    print(f"  • Using column: {time_column}")
    # Additional time analysis could go here
    print()

# STEP 6: VISUALIZE THE DATA
print("=" * 80)
print("STEP 6: VISUALIZE THE DATA")
print("=" * 80)
print()

# Visualization 1: Top bird species
if 'Bird Species' in data.columns:
    print("Creating visualization 1: Top 10 Bird Species...")
    top_10_species = data['Bird Species'].value_counts().head(10)
    
    plt.figure(figsize=(12, 6))
    plt.barh(range(len(top_10_species)), top_10_species.values, color='steelblue')
    plt.yticks(range(len(top_10_species)), top_10_species.index)
    plt.xlabel('Number of Strikes', fontsize=12)
    plt.ylabel('Bird Species', fontsize=12)
    plt.title('Top 10 Bird Species Involved in Strikes', fontsize=14, fontweight='bold')
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig('birds_top_species.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  ✅ Saved as 'birds_top_species.png'")
    print()

# Visualization 2: Distribution of another variable
# Check what columns are available for interesting visualizations
numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
if len(numeric_columns) > 0:
    print("Creating visualization 2: Numeric data distribution...")
    col_to_plot = numeric_columns[0]
    
    plt.figure(figsize=(10, 6))
    data[col_to_plot].hist(bins=30, color='teal', edgecolor='black', alpha=0.7)
    plt.xlabel(col_to_plot, fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title(f'Distribution of {col_to_plot}', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('birds_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  ✅ Saved as 'birds_distribution.png'")
    print()

# STEP 7: DRAW CONCLUSIONS
print("=" * 80)
print("STEP 7: DRAW CONCLUSIONS")
print("=" * 80)
print()

print("Key Findings:")
print("-" * 80)
print(f"  1. We analyzed {total_strikes:,} bird strike incidents")

if 'Bird Species' in data.columns:
    most_common_species = data['Bird Species'].value_counts().index[0]
    most_common_count = data['Bird Species'].value_counts().values[0]
    print(f"  2. Most common species: {most_common_species} ({most_common_count} incidents)")

print()
print("Implications:")
print("-" * 80)
print("  • This data can help airports implement targeted bird control measures")
print("  • Understanding patterns helps improve aircraft safety procedures")
print("  • Airlines can use this data for pilot training and awareness")
print()

# STEP 8: NEXT STEPS
print("=" * 80)
print("STEP 8: NEXT STEPS & RECOMMENDATIONS")
print("=" * 80)
print()
print("What you could do next:")
print("  • Analyze temporal patterns (time of day, season)")
print("  • Investigate geographical patterns (airports, regions)")
print("  • Correlate with aircraft types or flight phases")
print("  • Build a predictive model for high-risk conditions")
print("  • Create an interactive dashboard for stakeholders")
print()

# FINAL SUMMARY
print("=" * 80)
print("CONGRATULATIONS! YOU'VE COMPLETED A REAL DATA SCIENCE PROJECT!")
print("=" * 80)
print()
print("You practiced the complete data science workflow:")
print("  ✓ Step 1: Defined clear questions to answer")
print("  ✓ Step 2: Loaded real-world data")
print("  ✓ Step 3: Explored the data structure")
print("  ✓ Step 4: Cleaned and prepared the data")
print("  ✓ Step 5: Analyzed the data to find patterns")
print("  ✓ Step 6: Visualized findings")
print("  ✓ Step 7: Drew meaningful conclusions")
print("  ✓ Step 8: Identified next steps")
print()
print("This is the same process data scientists use in real projects!")
print()
print("Your next challenge:")
print("  • Try this workflow with other datasets in the data/ folder")
print("  • Come up with your own questions and find answers")
print("  • Share your findings with others")
print("=" * 80)
