class Books():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} written by {self.author}."
    
    def __len__(self):
        return self.pages
    
book1 = Books("King of Greed","Ana Huang",470)
print(book1)
print(f"It is {len(book1)} pages long!")