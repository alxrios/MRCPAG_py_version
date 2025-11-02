
class bookClass:
    def __init__(self, title = "", current_page = 0, total_pages = 1, url = ""):
        self.__title = title
        self.__total_pages = total_pages
        if total_pages > 0:
            self.__total_pages = total_pages
        else:
            self.__total_pages = 1 # default value is 1 for avoid division by
            # zero in __calculate_progress function.
        if current_page <= total_pages:
            self.__current_page = current_page
        else:
            self.__current_page = 0
        self.__url = url
        
    def print_book(self):
        """
        Prints the elements of the book object into the console.
        
        Returns
        -------
        None.

        """
        print("----------------------------------")
        print("Title: ", self.__title)
        print("Current page: ", self.__current_page)
        print("Total number of pages: ", self.__total_pages)
        print("Progress: ", self.__calculate_progress(), self.__progress_bar())
        print("Url: ", self.__url)
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
        i = 0 # i is initialized to 0 preventing the case in which the for loop
        # does not initializes
        for i in range(0, int(10*round(self.__current_page/self.__total_pages, 1))):
            bar += "#"
        
        if i < 9:
            bar += "..."
        
        bar += "]"
        
        return bar
        
        
































