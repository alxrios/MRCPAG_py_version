
import shelf_class

class menuClass:
    
    def menu_display(self):
        # Let's create one shelf object for each file and load the data.
        # shelf1 = shelf_class.shelfClass()
        # shelf2 = shelf_class.shelfClass()
        # shelf3 = shelf_class.shelfClass()
        # shelf4 = shelf_class.shelfClass()
        # shelf1.load_data(1)
        # shelf2.load_data(2)
        # shelf3.load_data(3)
        # shelf4.load_data(4)
        shelf = shelf_class.shelfClass()
        
        options_message = """
Choose an option:
1. Print the shelf.
2. Actualize current page of a book.
3. Delete a book.
4. Rename a book.
5. Actualize the total number of pages of a book.
6. Change file.
9. End program.

..."""
        option_file = input("Which file do you want to use? (1/2/3/4): ")
        while option_file not in ["1", "2", "3", "4"]:
            option_file = input("Which file do you want to use? (1/2/3/4): ")
            
        option_file = int(option_file)
        shelf.load_data(option_file)
        option_menu = input(options_message)
        
        while option_menu not in ["1", "2", "3", "4", "5", "6", "9"]:
            option_menu = input(options_message)
            
        option_menu = int(option_menu)
        
        while option_menu != 9:
            
            if option_menu == 1:
                shelf.print_shelf()
                option_menu = input(options_message)
                
                while option_menu not in ["1", "2", "3", "4", "5", "6", "9"]:
                    option_menu = input(options_message)
                    
                option_menu = int(option_menu)
                
            elif option_menu == 2:
                success = False
                book_to_actualize_p = input("Index of the book you want to actualize its current page: ")
                # First let's check that the user entered an integer.
                while not success:
                    try:
                        book_to_actualize_p = int(book_to_actualize_p)
                        success = True
                    except:
                        book_to_actualize_p = input("Index of the book you want to actualize its current page: ")
                # Check if the index entered is between 0 and the number of elements in the shelf
                success = False
                while not success:
                    if book_to_actualize_p >= 0 and book_to_actualize_p < shelf.get_n_elements():
                        success = True
                    else:
                        book_to_actualize_p = input("Please, introduce a number between 1 and " + str(shelf.get_n_elements()))




try:
    test = int("s")
except:
    print("not succesful")


success = False
test = input("index of blah blah blah")
while not success:
    # test = input("index of blah blah blah")
    try:
        test = int(test)
        success = True
    except:
        test = input("index of blah blah blah again: ")

# Function to contain the code with the while loop for checking if the input is int
# It's a try
def check_int(message):
    success = False
    input_user = input(message)
    while not success:
        try:
            input_user = int(input_user)
            success = True
        except:
            input_user = input(message)
    return input_user
            
            
# Let's test it
check_int("index of blah blah blah")

def ask_option():
    options_message = """
Choose an option:
1. Print the shelf.
2. Actualize current page of a book.
3. Delete a book.
4. Rename a book.
5. Actualize the total number of pages of a book.
6. Change file.
9. End program.

..."""
    option_keyboard = input(options_message)
    while option_keyboard not in ["1", "2", "3", "4", "5", "6", "9"]:
        option_keyboard = input(options_message)
    return int(option_keyboard)















