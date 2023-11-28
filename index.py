# imporing pymongo to establish connection
import pymongo
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://vedanshbalooni07:vedlms@cluster0.whqsdnz.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
# creating a database named Lib_man_sys
db=client['Lib_man_sys']

# creating a collection in the database named BOOKS
collection = db["books"]

# function to add a book
def add_book(title, author, genre):
    book = {"title": title, "author": author, "genre": genre}
    collection.insert_one(book)
    print("Book added successfully!")

# function to search for a book
# '$regex' is a generalized way to match patterns with sequences of characters
# the '$options' field allows you to specify additional settings for the regular expression
# "i" enables the user to make the matching field case insensitive
def search_book(query):
    results=collection.find({"$or":[{"title":{"$regex":query,"$options":"i"}},
                                    {"author":{"$regex":query,"$options":"i"}},
                                    {"genre":{"$regex":query,"$options":"i"}}]})
    if results.count()==0:
        print("No book found")
    else:
        print("Book found: ")
        for i in results:
            print(i)
            
# function to delete book
def delete_book(title):
    result=collection.delete_one({"title":title})
    if result.deleted_count==1:
        print("Book successfully deleted!")
    else:
        print("Book not found")
    
# function to update details of a book
def update_details(title, new_author=None, new_genre=None):  
    update_details={}
    if new_author:
        update_details["author"]=new_author
    if new_genre:
        update_details["genre"]=new_genre
    if not update_details:
        print("No fields provided")
    result = collection.update_one({"title":title},{"$set":update_details})
    
    if result.modified_count==1:
        print("Details have been updated")
    else:
        print("Book not found")
    
while True:
    print("\nBook Management System")
    print("1. Add a book")
    print("2. Search for a book")
    print("3. Delete book")
    print("4. Update book details")
    
    choice = input("Enter your choice from 1-4 options: ")
    
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        add_book(title, author, genre)

    elif choice == "2":
        query = input("Enter search query: ")
        search_book(query)

    elif choice == "3":
        title = input("Enter the title of the book to delete: ")
        delete_book(title)
        
    elif choice == "4":
        title = input("Enter the title of the book to update: ")
        new_author = input("Enter new author: ")
        new_genre = input("Enter new genre: ")
        update_details(title, new_author, new_genre)
        
    else:
        print("Invalid choice. Enter your no. again")