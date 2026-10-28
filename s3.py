class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PatientQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_patient(self, name):
        new_node = Node(name)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print("Patient added to queue!")

    def treat_patient(self):
        if self.front is None:
            print("No patients waiting!")
            return

        patient = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print("Now treating:", patient)

    def display_patients(self):
        if self.front is None:
            print("No patients waiting!")
            return

        current = self.front

        print("\nWaiting Patients:")

        while current:
            print(current.data)
            current = current.next


def main():
    hospital = PatientQueue()

    while True:
        print("\n===== HOSPITAL MANAGEMENT =====")
        print("1. Add Patient")
        print("2. Treat Next Patient")
        print("3. Display Waiting Patients")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter patient name: ").strip()

            if name:
                hospital.add_patient(name)
            else:
                print("Name cannot be empty!")

        elif choice == "2":
            hospital.treat_patient()

        elif choice == "3":
            hospital.display_patients()

        elif choice == "4":
            print("Exiting Hospital Management System!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
