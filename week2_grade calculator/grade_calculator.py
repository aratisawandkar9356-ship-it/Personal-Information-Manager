
# Student Grade Calculator
# Week 2 - Control Flow & Data Structures
# Author: Arati Sawandkar

# Function to calculate grade and comment
def calculate_grade(average):
    if average >= 90:
        return "A", "Excellent! Keep it up!"
    elif average >= 80:
        return "B", "Very Good! You are doing well."
    elif average >= 70:
        return "C", "Good. Keep improving."
    elif average >= 60:
        return "D", "Needs Improvement. Study more."
    else:
        return "F", "Failed. Please work harder."


# Function to get valid marks
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"{subject}: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Enter numbers only.")


# Function to display results
def display_results(results):
    print("\n" + "=" * 85)
    print("                         RESULTS SUMMARY")
    print("=" * 85)

    print(f"{'Name':<20} {'Math':>7} {'Science':>9} "
          f"{'English':>9} {'Average':>9} {'Grade':>7}")
    print("-" * 85)

    for student in results:
        print(
            f"{student['name']:<20}"
            f"{student['marks'][0]:>7.1f}"
            f"{student['marks'][1]:>9.1f}"
            f"{student['marks'][2]:>9.1f}"
            f"{student['average']:>9.1f}"
            f"{student['grade']:>7}"
        )
        print(f"  Comment: {student['comment']}")

    print("=" * 85)


# Function to search for a student
def search_student(results):
    search_name = input("\nEnter student name to search: ").strip()

    for student in results:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])
            print("Comment:", student["comment"])
            return

    print("Student not found!")


# Function to save results
def save_results(results):
    with open("results_sample.txt", "w", encoding="utf-8") as file:
        file.write("STUDENT GRADE CALCULATOR RESULTS\n")
        file.write("=" * 60 + "\n")

        for student in results:
            file.write(f"\nName: {student['name']}\n")
            file.write(f"Marks: {student['marks']}\n")
            file.write(f"Average: {student['average']:.2f}\n")
            file.write(f"Grade: {student['grade']}\n")
            file.write(f"Comment: {student['comment']}\n")

        averages = [student["average"] for student in results]

        if averages:
            file.write("\nCLASS STATISTICS\n")
            file.write(f"Total Students: {len(results)}\n")
            file.write(f"Class Average: {sum(averages)/len(averages):.2f}\n")
            file.write(f"Highest Average: {max(averages):.2f}\n")
            file.write(f"Lowest Average: {min(averages):.2f}\n")

    print("\nResults saved in results_sample.txt")


# Main function
def main():
    print("=" * 50)
    print("          STUDENT GRADE CALCULATOR")
    print("=" * 50)

    # Get number of students
    while True:
        try:
            num_students = int(input("\nEnter number of students: "))

            if num_students > 0:
                break
            else:
                print("Enter a positive number!")

        except ValueError:
            print("Invalid input! Enter a whole number.")

    # Create empty list
    results = []

    # Collect student information
    for i in range(num_students):
        print(f"\n--- STUDENT {i + 1} ---")

        name = input("Student name: ").strip()

        while name == "":
            print("Name cannot be empty!")
            name = input("Student name: ").strip()

        print("Enter marks (0-100):")
        math = get_valid_marks("Math")
        science = get_valid_marks("Science")
        english = get_valid_marks("English")

        marks = [math, science, english]
        average = sum(marks) / len(marks)

        grade, comment = calculate_grade(average)

        # Store student result in list
        results.append({
            "name": name,
            "marks": marks,
            "average": average,
            "grade": grade,
            "comment": comment
        })

    # Display results
    display_results(results)

    # Class statistics
    averages = [student["average"] for student in results]

    print("\nCLASS STATISTICS")
    print("-" * 40)
    print("Total Students:", len(results))
    print(f"Class Average: {sum(averages)/len(averages):.2f}")
    print(f"Highest Average: {max(averages):.2f}")
    print(f"Lowest Average: {min(averages):.2f}")

    # Menu system
    while True:
        print("\n1. Search Student")
        print("2. Save Results")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search_student(results)
        elif choice == "2":
            save_results(results)
        elif choice == "3":
            print("\nThank you for using Grade Calculator!")
            break
        else:
            print("Invalid choice! Select 1, 2 or 3.")


# Start program
if __name__ == "__main__":
    main()
