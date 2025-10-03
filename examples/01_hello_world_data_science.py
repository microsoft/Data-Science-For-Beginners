"""
Hello World - Data Science Style!

This is your very first data science program. It introduces you to the basic
concepts of working with data in Python.

What you'll learn:
- How to create a simple dataset
- How to display data
- How to work with Python lists and dictionaries
- Basic data manipulation

Prerequisites: Just Python installed on your computer!
"""

# Let's start with the classic "Hello, World!" but with a data science twist
print("=" * 50)
print("Hello, World of Data Science!")
print("=" * 50)
print()

# In data science, we work with data. Let's create our first simple dataset.
# We'll use a list to store information about students and their test scores.

# A list is a collection of items in Python, written with square brackets []
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 92, 78, 95, 88]

print("Our Dataset:")
print("-" * 50)
print("Students:", students)
print("Scores:", scores)
print()

# Now let's do something useful with this data!
# We can find basic statistics about the scores

# Find the highest score
highest_score = max(scores)
print(f"📊 Highest score: {highest_score}")

# Find the lowest score
lowest_score = min(scores)
print(f"📊 Lowest score: {lowest_score}")

# Calculate the average score
# sum() adds all numbers together, len() tells us how many items we have
average_score = sum(scores) / len(scores)
print(f"📊 Average score: {average_score:.2f}")  # .2f means show 2 decimal places
print()

# Let's find who got the highest score
# We use index() to find where the highest_score is in our list
top_student_index = scores.index(highest_score)
top_student = students[top_student_index]
print(f"🏆 Top student: {top_student} with a score of {highest_score}")
print()

# Now let's organize this data in a more structured way
# We'll use a dictionary - it pairs keys (student names) with values (scores)
print("Student Scores (organized as key-value pairs):")
print("-" * 50)

# Create a dictionary by pairing students with their scores
student_scores = {}
for i in range(len(students)):
    student_scores[students[i]] = scores[i]

# Display each student and their score
for student, score in student_scores.items():
    # Add a special marker for the top student
    marker = "⭐" if student == top_student else "  "
    print(f"{marker} {student}: {score} points")

print()
print("=" * 50)
print("Congratulations! You've completed your first data science program!")
print("=" * 50)

# What did we just do?
# 1. Created a simple dataset (student names and scores)
# 2. Performed basic analysis (max, min, average)
# 3. Found insights (who is the top student)
# 4. Organized the data in a useful structure (dictionary)
#
# These are the fundamental building blocks of data science!
# Next, you'll learn to work with real datasets using powerful libraries.
