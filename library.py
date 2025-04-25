library = []

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")
    genre = input("Genre: ")

    while True:
        read_input = input("Read? (yes/no): ").strip().lower()
        if read_input in ["yes", "no"]:
            read = read_input == "yes"
            break
        else:
            print("❌ Please enter 'yes' or 'no'.")

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print("✅ Book added!")

def remove_book():
    title = input("Title to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("🗑️ Book removed!")
            return
    print("❌ Book not found.")

def search_books():
    field = input("Search by title/author: ").lower()
    if field not in ["title", "author"]:
        print("❌ Please search by 'title' or 'author'.")
        return

    term = input(f"Enter {field}: ").lower()
    results = [b for b in library if term in b[field].lower()]
    
    if results:
        for b in results:
            status = "read" if b["read"] else "not read"
            print(f'📖 {b["title"]} by {b["author"]} ({b["year"]}) - {status}')
    else:
        print("❌ No books found.")

def show_books():
    if not library:
        print("📭 Library is empty.")
    else:
        for b in library:
            status = "read" if b["read"] else "not read"
            print(f'📘 {b["title"]} by {b["author"]} ({b["year"]}) - {status}')

def stats():
    total = len(library)
    read = sum(1 for b in library if b["read"])
    percent = (read / total) * 100 if total else 0
    print(f"📚 Total: {total}")
    print(f"✅ Read: {read}")
    print(f"📈 % Read: {percent:.2f}%")

def main():
    while True:
        print("\n📚 Library Menu:")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search Books")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            show_books()
        elif choice == "5":
            stats()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1-6.")

if __name__ == "__main__":
    main()

