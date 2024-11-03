"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.py"

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    with open(FILENAME) as input_file:
        compiled_data = []
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            compiled_data.append(parts)
        return compiled_data

def read_data(data):
    for subject, lecturer, students in data:
        print(f"{subject} is taught by {lecturer} and has {students} students")

def main():
    data = load_data()
    read_data(data)

main()