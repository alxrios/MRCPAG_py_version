
import shelf_class

# TO DO: Add another option to option menu that ask the user to change file.
#        Another function and option to move a book inside the current shelf.

class menuClass:
    
    def __ask_file(self):
        choosen_file = input("Which file do you want to use? (1/2/3/4): ")
        while choosen_file not in ["1", "2", "3", "4"]:
            choosen_file = input("Which file do you want to use? (1/2/3/4): ")
            
        return(int(choosen_file))
    
    def __ask_option_menu(self):
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
    
    def __check_book_index(self, message, num_of_books):
        success = False
        ask_input = input(message)
        while not success:
            try:
                ask_input = int(ask_input)
                ask_input -= 1 # User will see the indexes from 1 while lists
                # start at 0.
                # Once the input is an integer it must be inside the range from
                # 0 to the number of books in the shelf.
                if ask_input >= 0 and ask_input < num_of_books:
                    success = True
                else:
                    ask_input = input(message)
            except:
                ask_input = input(message)
        
        return ask_input
    
    def __ask_new_current_p(self, total):
        return self.__check_book_index("Introduce the new current page: ", total) + 1
    
    def menu_display(self):
        
        shelf = shelf_class.shelfClass()
        
        option_file = self.__ask_file()
        shelf.load_data(option_file)
        option_menu = self.__ask_option_menu()
        
        while option_menu != 9:
            
            if option_menu == 1:
                shelf.print_shelf()
                option_menu = self.__ask_option_menu()
                
            elif option_menu == 2:
                # Note: after changing the current page file should be rewritten
                # to save the changes.
                # Page introduced should be less than the total number of pages.
                #
                # Get the index of the book to actualize its current page.
                book_to_actualize_p = self.__check_book_index("Index of the book you want to actualize its current page: ", shelf.get_n_elements())
                # Ask for the new current page
                new_current_p = self.__ask_new_current_p(shelf.get_book_total_p(book_to_actualize_p))
                # Add the book to the shelf:
                shelf.add_book(shelf.get_book_title(book_to_actualize_p), 
                               new_current_p,
                               shelf.get_book_total_p(book_to_actualize_p),
                               shelf.get_book_file_path(book_to_actualize_p),
                               False,
                               book_to_actualize_p)
                # Write the file to save the changes
                shelf.write_file(option_file)
                # Presents again the menu with the options
                option_menu = self.__ask_option_menu()
            # elif option_menu == 3:
            #     print("")










