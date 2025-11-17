
import shelf_class
import book_class


class menuClass:
    
    def __ask_file(self):
        """
        Asks the user which file it wants to use.

        Returns
        -------
        None.

        """
        choosen_file = input("Which file do you want to use? (1/2/3/4): ")
        while choosen_file not in ["1", "2", "3", "4"]:
            choosen_file = input("Which file do you want to use? (1/2/3/4): ")
            
        return(int(choosen_file))
    
    def __ask_option_menu(self):
        options_message = """
    Choose an option:
    1. Print the shelf.
    2. Actualize current page of a book.
    3. Actualize the total number of pages of a book.
    4. Rename a book.
    5. Delete a book.
    6. Move a book.
    7. Change file.
    9. End program.

    ..."""
        option_keyboard = input(options_message)
        while option_keyboard not in ["1", "2", "3", "4", "5", "6", "7", "9"]:
            option_keyboard = input(options_message)
        return int(option_keyboard)
    
    def __check_book_index(self, message, num_of_books):
        """
        Ask the user to imput the index of a book in the shelf a checks that
        it is an integer between 1 and the total number of books in the shelf.

        Parameters
        ----------
        message : str
            Message to be printed to the user.
        num_of_books : int
            Number of books in the shelf.

        Returns
        -------
        ask_input : int
            Book's index introduced by the user minus one.

        """
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
        """
        Aks the user to introduce the new current page of a book, and checks
        if it's a valid value.

        Parameters
        ----------
        total : int
            Total number of pages of the book.

        Returns
        -------
        int
            New current page introduced by the user.

        """
        return self.__check_book_index("Introduce the new current page: ", total) + 1
    
    def __ask_new_total(self, current_page, book_index):
        """
        Asks the user to introduce the new total number of pages and checks if
        it can be a correct cipher.

        Parameters
        ----------
        current_page : int
            Current page for the book. The new total given by the user can be
            less than this cipher.
        book_index : int
            Location of the book in the shelf.

        Returns
        -------
        new_total : int
            New total introduced by the user.

        """
        message = "Introduce the new total of pages for the book " + str(book_index + 1) + ": "
        new_total = input(message)
        success = False
        while not success:
            try:
                new_total = int(new_total)
                if new_total >= current_page:
                    success = True
                else:
                    new_total = input(message)
            except:
                new_total = input(message)
                    
        return new_total
    
    def menu_display(self):
        """
        Displays the menu to interact with the user.

        Returns
        -------
        None.

        """
        
        shelf = shelf_class.shelfClass()
        
        option_file = self.__ask_file()
        shelf.load_data(option_file)
        option_menu = self.__ask_option_menu()
        
        while option_menu != 9:
            
            if option_menu == 1:
                shelf.print_shelf()
                option_menu = self.__ask_option_menu()
                
            elif option_menu == 2:
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
                
            elif option_menu == 3:
                book_index = self.__check_book_index("Index of the book to be modified: ", shelf.get_n_elements())
                new_total = self.__ask_new_total(shelf.get_book_current_p(book_index), book_index)
                shelf.add_book(shelf.get_book_title(book_index), 
                               shelf.get_book_current_p(book_index),
                               new_total,
                               shelf.get_book_file_path(book_index),
                               False,
                               book_index)
                shelf.write_file(option_file)
                option_menu = self.__ask_option_menu()
        
            elif option_menu == 4:
                book_index = self.__check_book_index("Index of the book to be renamed: ", shelf.get_n_elements())
                new_title = input("Introduce the new title: ")
                shelf.add_book(new_title, 
                               shelf.get_book_current_p(book_index),
                               shelf.get_book_total_p(book_index),
                               shelf.get_book_file_path(book_index),
                               False,
                               book_index)
                shelf.write_file(option_file)
                option_menu = self.__ask_option_menu()
            
            elif option_menu == 5:
                book_index = self.__check_book_index("Index of the book to be deleted: ", shelf.get_n_elements())
                shelf.delete_book(book_index)
                shelf.write_file(option_file)
                option_menu = self.__ask_option_menu()
            
            elif option_menu == 6:
                origin = self.__check_book_index("Index of the book to be moved: ", shelf.get_n_elements())
                destination = self.__check_book_index("Destination of the book to be moved: ", shelf.get_n_elements())
                aux_book = book_class.bookClass(shelf.get_book_title(destination), 
                                                shelf.get_book_current_p(destination),
                                                shelf.get_book_total_p(destination),
                                                shelf.get_book_file_path(destination))
                shelf.add_book(shelf.get_book_title(origin), 
                               shelf.get_book_current_p(origin),
                               shelf.get_book_total_p(origin),
                               shelf.get_book_file_path(origin),
                               False,
                               destination)
                shelf.add_book(aux_book.get_title(), 
                               aux_book.get_current_p(),
                               aux_book.get_total_p(),
                               aux_book.get_file_path(),
                               False,
                               origin)
                shelf.write_file(option_file)
                option_menu = self.__ask_option_menu()
            
            elif option_menu == 7:
                option_file = self.__ask_file()
                shelf.load_data(option_file)
                option_menu = self.__ask_option_menu()
                












