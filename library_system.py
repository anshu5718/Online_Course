
"""5. Library System
Q: Menu:
1. Add book
2. Issue book
3. Return book
4. Display books
5. Exit
Hint:
● Use dictionary to store book name → availability
(True/False)"""


Menu="""
Menu:
1. Add book
2. Issue book
3. Return book
4. Display books
5. Exit 
"""
def library():
    id=0
    book={}
    issued={}
    id_issued=0
    while True:
        print("**********************************")
        print(Menu)
        print("**********************************")
        choice=int(input("Enter a choice: "))
        if choice==1:
            new_book=input("Enter the name of the book you wanna add: ")
            duplicate=False
            for key,val in book.items():
                if val.lower()==new_book.lower():
                    duplicate=True
                    break
            if duplicate:
                print("Already entered")
                print("**********************************")
            else:
                id+=1
                book[id]=new_book
                print("New book added")
                print("**********************************")
        elif choice==2:
            wanted_book=input("Enter a name of the book you want to take: ")
            for key, val in list(book.items()):
                if wanted_book.lower()==val.lower():
                    id_issued+=1
                    name=input("Enter name of the person who want book: ")
                    issued[id_issued]=(name, wanted_book)
                    print("Done data entry: ")
                    del book[key]
                    book={i+1:v for i,v in enumerate(book.values())}
                    print("**********************************")
                    break
                else:
                    print("Book not found")
                    print("**********************************")
        elif choice==3:
            returned_book=input("Enter name of the returned book: ")
            id+=1
            book[id]=returned_book
            book = {i + 1: v for i, v in enumerate(book.values())}
            print("Updated list")
            print("**********************************")

        elif choice==4:
            for key,val in book.items():
                print(f"{key}: {val}")
                print("**********************************")
        elif choice==5:
            print("Thank you")
            break
        else:
            print("Enter correct choice: ")
library()

    

        


