class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        
    def check_availability(self):
        if self.available:
            print(f"{self.title} is available.")
        else:
            print(f"{self.title} is not available.")