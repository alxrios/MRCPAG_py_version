
class bookClass:
    def __init__(self, title = "", current_page = 0, total_pages = 0):
        self.title = title
        self.current_page = current_page
        self.total_pages = total_pages
        
    def print_book(self):
        print(self.title)
        print(self.current_page)
        print(self.total_pages)
        print("----------------------------------")
        print("Title: ", self.title)
        print("Current page: ", self.current_page)
        print("Total number of pages: ", self.total_pages)
        print("----------------------------------")
        
        
        
        
        
test = bookClass("myBook", 5, 100)
test.print_book()