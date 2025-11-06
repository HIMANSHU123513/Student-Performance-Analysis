import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset (example data)
data = {
    'Name': ['Anil', 'Bhumika', 'Chetan', 'Divya', 'Esha', 'Farhan'],
    'Maths': [78, 93, 85, 66, 74, 88],
    'Science': [82, 89, 91, 72, 68, 94],
    'English': [75, 85, 79, 80, 70, 90],
    'Hindi': [85, 80, 73, 91, 97, 69],
    'Attendance(%)': [90, 95, 92, 80, 75, 97]
}

result = pd.DataFrame(data)

# Step 2: Calculate total & average marks
result['Total'] = result[['Maths', 'Science', 'English','Hindi']].sum(axis=1)
result['Average'] = result['Total'] / 3

# Step 3: Grade calculation
def grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'D'

result['Grade'] = result['Average'].apply(grade)

# Step 4: Print summary
print("Student Performance Summary:\n")
print(result)

# Step 5: Visualization
plt.bar(result['Name'], result['Average'], color='skyblue')
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()
