students = []

def add_student():
    name = input("Enter student name: ")

    try:
        marks = float(input("Enter marks out of 100: "))

        if marks < 0 or marks > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            return

        student = {"name": name, "marks": marks}
        students.append(student)

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")


def display_ranking():
    if not students:
        print("No student records available!")
        return

    ranking = sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )

    print("\n========== STUDENT RANKING ==========")
    print("{:<10} {:<20} {:<10}".format("Rank", "Name", "Marks"))
    print("-" * 40)

    for rank, student in enumerate(ranking, start=1):
        print("{:<10} {:<20} {:<10.2f}".format(
            rank, student["name"], student["marks"]
        ))

    print("\nTopper:", ranking[0]["name"])
    print("Highest Marks:", ranking[0]["marks"])


while True:
    print("\n===== STUDENT RANKING SYSTEM =====")
    print("1. Add Student")
    print("2. Display Ranking")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_ranking()

    elif choice == "3":
        print("Thank you for using Student Ranking System!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")