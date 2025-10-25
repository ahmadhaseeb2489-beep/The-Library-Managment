#making a simple library manger
import json

def main():
    library = load_book()
    print("\n welcome to your personal library manager")
    while True:
        print("\n Enter '1' to shw all the book from your library")
        print("\n Enter '2' to add new book")
        print("\n Enter '3' to remove book from your library")
        print("\n Enter '4' to search book from your library")
        print("\n Enter '5' to count your books from library ")
        print("\n Enter '6' to save and exit")
        choice = input("\n Enter your choice from (1-5): ") #for user input to make choices
        if choice == "1":
            view_book(library)
        elif choice == "2":
            add_book(library)
        elif choice == "3":
            remove_book(library)
        elif choice == "4":
            search_book(library)
        elif choice == "5":
            count_book(library)
        elif choice == "6":
            save_book(library)
            print("books are saved to file.")
            print('thank you for using persnol library manager')
            break

        else:
                print('please enter a valid choice')
def load_book(): #to open a file
    try:
        with open("my_library.json","r") as file:
            return json.load(file)
    except (FileNotFoundError , json.JSONDecodeError):
        return []
def save_book(library): # for saving book to file
    with open("my_library.json", "w") as file:
        json.dump(library, file, indent=4)

def view_book(library):
    if not library:
        print("sorry! your library is empty ")
        return
    print(f"\n your books ({len(library)}total):")
    print("-"* 30)
    for i, books in enumerate(library , 1):
        print(f"{i}. {books['title']} by {books['author']} ({books['year']})")
        print(f"       Status: {books['status']}")
        print()

def add_book(library):
        title = input("enter your book title: ").strip()
        author = input("enter your book author: ").strip()
        year = input("enter your book year: ").strip()
        if title and author:
            book ={
                "title": title,
                "author": author,
                "year": year,
                "status" : "unread"
            }
            library.append(book)
            save_book(library)
            print(f"{title}is added to your library")
        else:
            print("please enter your book title and author")



def remove_book(library):
    if not library:
        print("sorry! there are no books to remove ")
        return
    view_book(library)
    try:
        book_num = int(input("\n enter your book number to remove: "))
        if 1 <= book_num <= len(library):
            removed_book = library.pop(book_num - 1)  # FIXED: minus sign, not comma
            print(f"\n {removed_book} has been removed from library")
            save_book(library)
        else:
            print("sorry! you have entered invalid book number")
    except ValueError:
        print("please enter a valid book number")


def search_book(library):
    if not library:
        print("sorry! your library is empty ")
        return

    print("\n=== SEARCH BOOKS ===")
    print("1. Search by title")
    print("2. Search by author")

    search_choice = input("Choose search type (1,2): ")
    if search_choice == 1:
        input("Enter title: ").lower().strip()
    else:
        input("Enter author: ").lower().strip()

    found_books = []

    if search_choice == "1":
        found_books = [book for book in library if search_choice in book['title'].lower()]
    elif search_choice == "2":
        found_books = [book for book in library if search_choice in book['author'].lower()]
    else:
        print("Invalid search choice!")
        return

    if found_books:
        print(f"\n Found {len(found_books)} book(s):")
        print("-" * 50)
        for i, book in enumerate(found_books, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']})")
            print(f"          Status: {book['status']}")
            print()
    else:
        print(" No books found!")

def count_book(library):
    print(f"you have {len(library)} books in library")
    print("-"* 30)
if __name__ == "__main__":
    main()