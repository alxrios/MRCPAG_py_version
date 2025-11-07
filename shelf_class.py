
import book_class

class shelfClass:
    def __init__(self, n_elements = 0):
        if n_elements >= 0:
            self.__n_elements = n_elements
        else:
            self.__n_elements = 0
        
        self.__shelf = []
        for i in range(0, self.__n_elements):
            self.__shelf.append(book_class.bookClass())
        
    def get_n_elements(self):
        """
        Returns the number of elements in the shelf.

        Returns
        -------
        int
            Number of elements in the shelf.

        """
        return self.__n_elements
    
    def __set_n_elements(self, new_n_elements):
        """
        Actualizes the number of elements accounted in the variable n_elements.

        Parameters
        ----------
        new_n_elements : int
            New number of elements in the shelf.

        Returns
        -------
        None.

        """
        if type(new_n_elements) == int and new_n_elements >= 0:
            self.__n_elements = new_n_elements
            
    
    def add_book_console(self, b_title = "", b_current_p = 0, b_total_p = 1, b_url = "", append = True, index = 0):
        """
        Adds a new book with the data passed through the parameters.

        Parameters
        ----------
        b_title : str, optional
            Book's title. The default is "".
        b_current_p : int, optional
            Current page of the book. The default is 0.
        b_total_p : int, optional
            Total pages of the book. The default is 1.
        b_url : str, optional
            Location in the disk of the book file. The default is "".
        append : bool, optional
            If True book is added at the end of the current
            list, if False it's added in the position . The default is True.
        index : int, optional
            Possition to add the new book if parameter append is put to False. 
            The default is 0.

        Returns
        -------
        None.

        """
        if append:
            self.__shelf.append(book_class.bookClass(b_title, b_current_p, 
                                                     b_total_p, b_url))
            
            # Actualize the number of elements in the shelf.
            self.__set_n_elements(self.get_n_elements() + 1)
        else:
            # The index in which the new book is desired to be must be between
            # the current size of the list.
            if index < self.get_n_elements():
                self.__shelf[index] = book_class.bookClass(b_title,
                                                           b_current_p, 
                                                           b_total_p, b_url)
                
    def print_shelf(self):
        """
        Prints the information of the books contained in the shelf.

        Returns
        -------
        None.

        """
        for i in range(0, self.get_n_elements()):
            print(str(i + 1) + ".")
            self.__shelf[i].print_book()
            
    def load_data(self, option = 1):
        # First change the current directory if it's not located where the
        # files are in. (Files are supossed to be in a directory called 
        # mrcpag_files located in the previous folder where the script will be
        # executed).
        import os
        splitted_dir = os.getcwd().split("\\")
        if splitted_dir[len(splitted_dir) - 1] != "mrcpag_files":
            os.chdir("../mrcpag_files")
        # Once in the correct directory, we obtain the names of the files.
        # The one that would be read will be determined by the parameter option.
        list_of_files = os.listdir()
        # Before load any new data, let's clear any existing one in the shelf.
        self.__shelf = []
        self.__set_n_elements(0)
        if option == 1:
            counter = 0 # Auxiliar variable for counting the lines read.
            readList = [] # An auxiliar list for storing the lines.
            with open(list_of_files[4]) as file:
                for line in file:
                    counter += 1
                    readList.append(line.rstrip())
                    if counter == 4:
                        self.__shelf.append(book_class.bookClass(readList[0], int(readList[1]), 
                                                             int(readList[2]), readList[3]))
                        
                        self.__set_n_elements(self.get_n_elements() + 1)
                        readList = []
                        counter = 0
        
        elif option == 2:
            counter = 0
            readList = []
            with open(list_of_files[1]) as file:
                for line in file:
                    counter += 1
                    readList.append(line.rstrip())
                    if counter == 5:
                        self.__shelf.append(book_class.bookClass(readList[1], int(readList[2]), 
                                                             int(readList[3]), readList[4], readList[0], has_sub1 = True))
                        self.__set_n_elements(self.get_n_elements() + 1)
                        readList = []
                        counter = 0
        
        elif option == 3:
            counter = 0
            readList = []
            with open(list_of_files[2]) as file:
                for line in file:
                    counter += 1        
                    readList.append(line.rstrip())
                    if counter == 6:
                        self.__shelf.append(book_class.bookClass(readList[2], int(readList[3]), int(readList[4]), readList[5], readList[0], readList[1], has_sub1 = True, has_sub2 = True))
                        self.__set_n_elements(self.get_n_elements() + 1)
                        readList = []
                        counter = 0
                        
        if option == 4:
            counter = 0 # Auxiliar variable for counting the lines read.
            readList = [] # An auxiliar list for storing the lines.
            with open(list_of_files[3]) as file:
                for line in file:
                    counter += 1
                    readList.append(line.rstrip())
                    if counter == 4:
                        self.__shelf.append(book_class.bookClass(readList[0], int(readList[1]), 
                                                             int(readList[2]), readList[3]))
                        
                        self.__set_n_elements(self.get_n_elements() + 1)
                        readList = []
                        counter = 0
            

