users = []
MAX_USERS = 20

matrix = [
    [0] * MAX_USERS for _ in range(MAX_USERS)
]


def add_user():
    if len(users) >= MAX_USERS:
        print("Maximum number of users reached!")
        return

    name = input("Enter user name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    if name in users:
        print("User already exists!")
        return

    users.append(name)
    print("User added successfully!")


def add_friendship():
    if len(users) < 2:
        print("Add at least two users first!")
        return

    print("Users:", ", ".join(users))

    user1 = input("Enter first user: ").strip()
    user2 = input("Enter second user: ").strip()

    if user1 not in users or user2 not in users:
        print("User not found!")
        return

    if user1 == user2:
        print("A user cannot be their own friend!")
        return

    i = users.index(user1)
    j = users.index(user2)

    matrix[i][j] = 1
    matrix[j][i] = 1

    print("Friendship added successfully!")


def display_network():
    if not users:
        print("No users available!")
        return

    print("\n===== FRIENDSHIP ADJACENCY MATRIX =====")

    print("{:<12}".format(""), end="")

    for user in users:
        print("{:<12}".format(user), end="")

    print()

    for i in range(len(users)):
        print("{:<12}".format(users[i]), end="")

        for j in range(len(users)):
            print("{:<12}".format(matrix[i][j]), end="")

        print()


def display_friends():
    name = input("Enter user name: ").strip()

    if name not in users:
        print("User not found!")
        return

    i = users.index(name)

    friends = [
        users[j]
        for j in range(len(users))
        if matrix[i][j] == 1
    ]

    if friends:
        print("Friends of", name, ":", ", ".join(friends))
    else:
        print("No friends found!")


while True:
    print("\n===== SOCIAL NETWORK SYSTEM =====")
    print("1. Add User")
    print("2. Add Friendship")
    print("3. Display Adjacency Matrix")
    print("4. Display Friends")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_user()

    elif choice == "2":
        add_friendship()

    elif choice == "3":
        display_network()

    elif choice == "4":
        display_friends()

    elif choice == "5":
        print("Exiting Social Network System!")
        break

    else:
        print("Invalid choice!")