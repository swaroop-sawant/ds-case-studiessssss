SIZE = 10


class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(SIZE)]

    def hash_function(self, word):
        return sum(ord(ch) for ch in word.lower()) % SIZE

    def add_word(self, word, meaning):
        index = self.hash_function(word)

        for entry in self.table[index]:
            if entry[0] == word.lower():
                entry[1] = meaning
                print("Meaning updated successfully!")
                return

        self.table[index].append([word.lower(), meaning])
        print("Word added successfully!")

    def search_word(self, word):
        index = self.hash_function(word)

        for entry in self.table[index]:
            if entry[0] == word.lower():
                print("Meaning:", entry[1])
                return

        print("Word not found!")

    def display_words(self):
        print("\n===== DICTIONARY ENTRIES =====")

        found = False

        for bucket in self.table:
            for word, meaning in bucket:
                print(word, ":", meaning)
                found = True

        if not found:
            print("Dictionary is empty!")

    def delete_word(self, word):
        index = self.hash_function(word)

        for entry in self.table[index]:
            if entry[0] == word.lower():
                self.table[index].remove(entry)
                print("Word deleted successfully!")
                return

        print("Word not found!")


dictionary = HashTable()


while True:
    print("\n===== DICTIONARY APPLICATION =====")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Display All Words")
    print("4. Delete Word")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter word: ").strip()
        meaning = input("Enter meaning: ").strip()

        if word and meaning:
            dictionary.add_word(word, meaning)
        else:
            print("Word and meaning cannot be empty!")

    elif choice == "2":
        word = input("Enter word to search: ").strip()
        dictionary.search_word(word)

    elif choice == "3":
        dictionary.display_words()

    elif choice == "4":
        word = input("Enter word to delete: ").strip()
        dictionary.delete_word(word)

    elif choice == "5":
        print("Exiting Dictionary Application!")
        break

    else:
        print("Invalid choice!")