def calculate_grade():
    num_subjects = int(input("Enter the number of subjects: "))
    subject_marks = []

    for i in range(num_subjects):
        while True:
            try:
                marks = float(input(f"Enter marks obtained (out of 100) for subject {i + 1}: "))
                if 0 <= marks <= 100:
                    subject_marks.append(marks)
                    break
                else:
                    print("Marks should be between 0 and 100. Please enter again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for marks.")

    total_marks = sum(subject_marks)
    average_percentage = total_marks / num_subjects if num_subjects > 0 else 0

    if 90 <= average_percentage <= 100:
        grade = "A+"
    elif 80 <= average_percentage < 90:
        grade = "A"
    elif 70 <= average_percentage < 80:
        grade = "B"
    elif 60 <= average_percentage < 70:
        grade = "C"
    elif 50 <= average_percentage < 60:
        grade = "D"
    else:
        grade = "F"

    print("\n--- Results ---")
    print(f"Total Marks: {total_marks}")
    print(f"Average Percentage: {average_percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    calculate_grade()
