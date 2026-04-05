# part1_grade_tracker.py

# ==========================================================
# Task 1 — Data Parsing & Profile Cleaning
# ==========================================================

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    # 1. cleaning name (extra spaces were there)
    clean_name = student["name"].strip().title()
    
    # 2. Convert roll to integer
    clean_roll = int(student["roll"])
    
    # 3. Convert marks_str to a list of integers
    # Splitting by ", " then using list comprehension to convert each item
    clean_marks = [int(m) for m in student["marks_str"].split(", ")]
    
    # Store cleaned data
    student_profile = {"name": clean_name, "roll": clean_roll, "marks": clean_marks}
    cleaned_students.append(student_profile)
    
    # Check if name is valid (alphabetical check for each word)
    is_valid = all(word.isalpha() for word in clean_name.split())
    status_icon = "✓ Valid name" if is_valid else "✗ Invalid name"
    
    # Print Profile Card
    print("=" * 32)
    print(f"Student : {clean_name}")
    print(status_icon)
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("=" * 32)

# Specific requirement for roll number 103
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"\nStudent 103 - Uppercase: {s['name'].upper()}")
        print(f"Student 103 - Lowercase: {s['name'].lower()}\n")


# ==========================================================
# Task 2 — Marks Analysis Using Loops & Conditionals
# ==========================================================

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"--- Analysis for {student_name} ---")
for i in range(len(subjects)):
    m = marks[i]
    # Determine Grade
    if m >= 90: grade = "A+"
    elif m >= 80: grade = "A"
    elif m >= 70: grade = "B"
    elif m >= 60: grade = "C"
    else: grade = "F"
    
    print(f"{subjects[i]:<10}: {m} ({grade})")

total = sum(marks)
avg = round(total / len(marks), 2)
print(f"\nTotal: {total} | Average: {avg}")

# Highest and Lowest scoring logic
high_idx = marks.index(max(marks))
low_idx = marks.index(min(marks))
print(f"Highest: {subjects[high_idx]} ({marks[high_idx]})")
print(f"Lowest: {subjects[low_idx]} ({marks[low_idx]})")

# While loop for new marks entry
print("\n--- Manual Entry Mode (type 'done' to stop) ---")
new_subjects_count = 0
while True:
    sub_input = input("Enter subject name: ").strip()
    if sub_input.lower() == 'done':
        break
    
    mark_input = input(f"Enter marks for {sub_input}: ")
    if mark_input.isdigit():
        m_val = int(mark_input)
        if 0 <= m_val <= 100:
            marks.append(m_val)
            new_subjects_count += 1
        else:
            print("Warning: Marks must be between 0-100.")
    else:
        print("Warning: Please enter a numeric value.")

new_avg = round(sum(marks) / len(marks), 2)
print(f"\nAdded {new_subjects_count} subjects. New Class Average: {new_avg}\n")


# ==========================================================
# Task 3 — Class Performance Summary
# ==========================================================

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print(f"{'Name':<18} | {'Average':<7} | {'Status'}")
print("-" * 40)

pass_count = 0
fail_count = 0
all_averages = []
topper_name = ""
max_avg = -1

for name, m_list in class_data:
    student_avg = round(sum(m_list) / len(m_list), 2)
    all_averages.append(student_avg)
    status = "Pass" if student_avg >= 60 else "Fail"
    
    if status == "Pass": pass_count += 1
    else: fail_count += 1
    
    if student_avg > max_avg:
        max_avg = student_avg
        topper_name = name
        
    print(f"{name:<18} |  {student_avg:<7.2f} | {status}")

print("-" * 40)
print(f"Passed: {pass_count} | Failed: {fail_count}")
print(f"Topper: {topper_name} ({max_avg})")
print(f"Class Overall Average: {round(sum(all_averages)/len(all_averages), 2)}\n")


# ==========================================================
# Task 4 — String Manipulation Utility
# ==========================================================

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# 1. Strip and store
clean_essay = essay.strip()
print(f"1. Cleaned Essay: {clean_essay}")

# 2. Title Case
print(f"2. Title Case: {clean_essay.title()}")

# 3. Count "python" (case-insensitive)
# Since clean_essay is already mostly lowercase from the source, we ensure it's lowered for accuracy
count_py = clean_essay.count("python")
print(f"3. Python Count: {count_py}")

# 4. Replace
replaced_essay = clean_essay.replace("python", "Python 🐍")
print(f"4. Replaced: {replaced_essay}")

# 5. Split into sentences
sentences = clean_essay.split(". ")
print(f"5. Sentences List: {sentences}")

# 6. Numbered sentences
print("\n6. Numbered Sentences:")
for i, sentence in enumerate(sentences, 1):
    # Ensure it ends with a period
    final_sentence = sentence.strip()
    if not final_sentence.endswith("."):
        final_sentence += "."
    print(f"{i}. {final_sentence}")
    
