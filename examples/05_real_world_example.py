"""
Real World Example: Complete Data Science Workflow

This example ties everything together, showing you a complete data science project
from start to finish. We'll analyze Minnesota bird species data to answer real questions.

What you'll learn:
- How to approach a data science problem
- Complete workflow: Load → Explore → Clean → Analyze → Visualize → Conclude
- How to handle real-world data issues
- How to draw meaningful conclusions

Prerequisites: 
- pandas library (install with: pip install pandas)
- matplotlib library (install with: pip install matplotlib)

Real-world context:
Understanding bird biodiversity and physical characteristics helps conservationists
and ecologists protect wildlife and monitor ecosystem health.
Let's analyze bird species data to understand patterns and conservation status.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

print("=" * 80)
print("REAL WORLD DATA SCIENCE PROJECT: BIRD SPECIES ANALYSIS")
print("=" * 80)
print()

# STEP 1: DEFINE THE PROBLEM
print("=" * 80)
print("STEP 1: DEFINE THE PROBLEM")
print("=" * 80)
print()
print("Questions we want to answer:")
print("  1. How many bird species are recorded?")
print("  2. What are the most common bird categories and families?")
print("  3. What is the conservation status distribution of these birds?")
print("  4. Which bird species are the largest (wingspan and body mass)?")
print()
input("Press Enter to continue...")
print()

# STEP 2: LOAD THE DATA
print("=" * 80)
print("STEP 2: LOAD THE DATA")
print("=" * 80)
print()
print("📂 Loading bird species data...")

# Resolve path relative to this script so it works from any directory
data_path = Path(__file__).resolve().parent.parent / 'data' / 'birds.csv'

try:
    data = pd.read_csv(data_path)
    print(f"✅ Successfully loaded {len(data)} records")
    print()
except FileNotFoundError:
    print(f"❌ Error: birds.csv not found at {data_path}")
    print("Please make sure the data file exists in data/ folder.")
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

# Analysis 1: Total number of species
total_species = len(data)
print("Analysis 1: Overview")
print("-" * 80)
print(f"  • Total bird species recorded: {total_species:,}")
print()

# Analysis 2: Most common bird categories
print("Analysis 2: Most Common Bird Categories")
print("-" * 80)
top_categories = data['Category'].value_counts().head(5)
for i, (category, count) in enumerate(top_categories.items(), 1):
    print(f"  {i}. {category}: {count} species ({count/total_species*100:.1f}%)")
print()

# Analysis 3: Conservation status distribution
print("Analysis 3: Conservation Status Breakdown")
print("-" * 80)
status_names = {
    'LC': 'Least Concern',
    'NT': 'Near Threatened',
    'VU': 'Vulnerable',
    'EN': 'Endangered',
    'CR': 'Critically Endangered',
    'EX': 'Extinct'
}
status_counts = data['ConservationStatus'].value_counts()
for code, count in status_counts.items():
    label = status_names.get(code, code)
    print(f"  • {label} ({code}): {count} species ({count/total_species*100:.1f}%)")
print()

# Analysis 4: Physical extremes
print("Analysis 4: Physical Extremes")
print("-" * 80)
heaviest = data.loc[data['MaxBodyMass'].idxmax()]
longest_wingspan = data.loc[data['MaxWingspan'].idxmax()]
print(f"  • Heaviest bird: {heaviest['Name']} ({heaviest['MaxBodyMass']:,} g)")
print(f"  • Largest wingspan: {longest_wingspan['Name']} ({longest_wingspan['MaxWingspan']:,} mm)")
print()

# STEP 6: VISUALIZE THE DATA
print("=" * 80)
print("STEP 6: VISUALIZE THE DATA")
print("=" * 80)
print()

# Visualization 1: Top 10 bird categories
print("Creating visualization 1: Top 10 Bird Categories...")
top_10_categories = data['Category'].value_counts().head(10)

plt.figure(figsize=(12, 6))
plt.barh(range(len(top_10_categories)), top_10_categories.values, color='steelblue')
plt.yticks(range(len(top_10_categories)), top_10_categories.index)
plt.gca().invert_yaxis()  # Put highest count at the top
plt.xlabel('Number of Species', fontsize=12)
plt.ylabel('Bird Category', fontsize=12)
plt.title('Top 10 Bird Categories in Minnesota', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('birds_top_categories.png', dpi=300, bbox_inches='tight')
plt.close()
print("  ✅ Saved as 'birds_top_categories.png'")
print()

# Visualization 2: Distribution of MaxWingspan
print("Creating visualization 2: Wingspan Distribution...")
plt.figure(figsize=(10, 6))
data['MaxWingspan'].hist(bins=30, color='teal', edgecolor='black', alpha=0.7)
plt.xlabel('Maximum Wingspan (mm)', fontsize=12)
plt.ylabel('Number of Species', fontsize=12)
plt.title('Distribution of Maximum Wingspan Across Bird Species', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('birds_wingspan_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("  ✅ Saved as 'birds_wingspan_distribution.png'")
print()

# STEP 7: DRAW CONCLUSIONS
print("=" * 80)
print("STEP 7: DRAW CONCLUSIONS")
print("=" * 80)
print()

print("Key Findings:")
print("-" * 80)
print(f"  1. We analyzed {total_species:,} distinct bird species")
most_common_cat = top_categories.index[0]
most_common_count = top_categories.values[0]
print(f"  2. Most common category: {most_common_cat} ({most_common_count} species)")
lc_count = status_counts.get('LC', 0)
print(f"  3. Conservation: {lc_count/total_species*100:.1f}% of species are Least Concern (LC)")
print(f"  4. The widest wingspan belongs to {longest_wingspan['Name']} ({longest_wingspan['MaxWingspan']:,} mm)")
print()

print("Implications:")
print("-" * 80)
print("  • Understanding bird biodiversity helps local conservation programs")
print("  • Monitoring threatened species (NT, VU, EN, CR) guides habitat protection")
print("  • Morphological data supports avian biology and ecological research")
print()

# STEP 8: NEXT STEPS
print("=" * 80)
print("STEP 8: NEXT STEPS & RECOMMENDATIONS")
print("=" * 80)
print()
print("What you could do next:")
print("  • Analyze correlation between wingspan and body mass")
print("  • Compare average physical measurements across different bird Orders")
print("  • Focus on threatened species to explore conservation priorities")
print("  • Build a machine learning classifier to predict bird category from measurements")
print("  • Create an interactive visualization dashboard")
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
