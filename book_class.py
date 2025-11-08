
class bookClass:
    def __init__(self, title = "", current_page = 0, total_pages = 1, file_path = "", subject1 = "", subject2 = "", has_sub1 = False, has_sub2 = False):
        self.__title = title
        self.__total_pages = total_pages
        if total_pages > 0:
            self.__total_pages = total_pages
        else:
            self.__total_pages = 1 # default value is 1 to avoid division by
            # zero in __calculate_progress function.
        if current_page <= total_pages:
            self.__current_page = current_page
        else:
            self.__current_page = 0
            
        self.__file_path = file_path
        self.__subject1 = subject1
        self.__subject2 = subject2
        self.__has_sub1 = has_sub1
        self.__has_sub2 = has_sub2
        
        
    def print_book(self):
        """
        Prints the elements of the book object into the console.
        
        Returns
        -------
        None.

        """
        print("----------------------------------")
        if self.__has_sub1 and self.__has_sub2:
            print(self.__subject1, "|", self.__subject2)
        elif self.__has_sub1:
            print(self.__subject1)
        print("Title: ", self.__title)
        print("Current page: ", self.__current_page)
        print("Total number of pages: ", self.__total_pages)
        print("Progress: ", self.__calculate_progress(), self.__progress_bar())
        print("File_path: ", self.__file_path)
        print("----------------------------------")
        
    def __calculate_progress(self):
        """
        Calculates the percentage of pages read.

        Returns
        -------
        str
            Percentage of pages already read.

        """
        return str(round(100*self.__current_page/self.__total_pages, 2)) + "%"
    
    def __progress_bar(self):
        """
        Returns
        -------
        bar : str
            A row of hashtags representing the percentage of pages read.

        """
        bar = "["
        i = 0 # i is initialized to 0 preventing the case in which the next for loop
        # does not initializes
        end_loop = int(10*round(self.__current_page/self.__total_pages, 1)) # Number
        # of hashtags that will contain the progress bar.
        for i in range(0, end_loop):
            bar += "#"
            
        if end_loop == 0:
            new_init = i # Beginning of the next loop.
        else:
            new_init = i + 1
        # Now dots are added, up to ten.
        for i in range(new_init, 10):
            bar += "."
        
        bar += "]"
        
        return bar
    
    def set_title(self, new_title = ""):
        """
        Changes the book's title to new_title

        Parameters
        ----------
        new_title : str, optional
            Content of the new title. The default is "".

        Returns
        -------
        None.

        """
        self.__title = new_title
        
    def set_current_p(self, new_current = 0):
        """
        Changes the current_page variable to the value passed in new_current.

        Parameters
        ----------
        new_current : int, optional
            New current page. The default is 0.

        Returns
        -------
        None.

        """
        if new_current >= 0 and new_current <= self.__total_pages:
            self.__current_page = new_current


    def set_total_p(self, new_total = 1):
        """
        Actualizes the total number of pages.

        Parameters
        ----------
        new_total : int, optional
            New value for the variable total_pages. The default is 1.

        Returns
        -------
        None.

        """
        if new_total > 0:
            self.__total_pages = new_total
    
    def set_file_path(self, new_file_path = ""):
        """
        Sets the new file's path

        Parameters
        ----------
        new_file_path : str, optional
            Location in disk of the book file. The default is "".

        Returns
        -------
        None.

        """
        self.__file_path = new_file_path

    def get_title(self):
        """
        Returns the books title.
        Returns
        -------
        str
            Book's title.

        """
        return self.__title

    def get_current_p(self):
        """
        Returns the current page.

        Returns
        -------
        int
            Book's current page.

        """
        return self.__current_page

    def get_total_p(self):
        """
        Returns the total number of pages.

        Returns
        -------
        int
            Book's total number of pages.

        """
        return self.__total_pages

    def get_file_path(self):
        """
        Returns the location of the book file.

        Returns
        -------
        str
            Location of the book file.

        """
        return self.__file_path

    def get_subject1(self):
        """
        Returns the value of subject1.

        Returns
        -------
        str
            Value stored in the variable subject1.

        """
        return self.__subject1
    
    def get_subject2(self):
        """
        Returns the value of subject2.

        Returns
        -------
        str
            Value stored in the variable subject2.

        """
        return self.__subject2
    
    def get_has_sub1(self):
        """
        Returns the value of has_sub1

        Returns
        -------
        bool
            True if subject1 has content different than the empty string, 
            and False otherwise.

        """
        return self.__has_sub1

    def get_has_sub2(self):
        """
        Returns the value of has_sub2

        Returns
        -------
        bool
            True if subject2 has content different than the empty string, 
            and False otherwise.

        """
        return self.__has_sub2









