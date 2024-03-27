class LinkedList:
  def __init__ (self, key, info):
    self.key = key
    self.info = info
    self.next = None


class Library():
    def __init__(self) -> None:
        self.library = []

    def __del__(self):
        pass

    def add_book(self, title, author):
        if(len(self.library) == 0):
            self.library.append(LinkedList(title, author))
            return

        i = 0
        while (i < len(self.library)):    #Ищу элемент с таким же ключом, нашел - добавляю его в конец с таким же ключом
                            
            if(title == self.library[i].key):
                bufer = self.library[i]
                while(bufer.next != None):
                    bufer = bufer.next
                bufer.next = LinkedList(title, author)
                return
            i += 1  
                 

        self.library.append(LinkedList(title, author))

    def find_book_by_author(self, author):
        i = 0; arr  = []
        while (i < len(self.library)):
            if(author == self.library[i].info):
                bufer = self.library[i]
                while(True):
                    arr.append(bufer.info)
                    if(bufer.next == None): break
                    bufer = bufer.next
            i += 1    
        if(arr == []):
            arr.append("Не нашел")     
        return arr  

    def find_book_by_title(self, title):
        i = 0; arr  = []
        while (i < len(self.library)):
            if(title == self.library[i].key):
                bufer = self.library[i]
                while(True):
                    arr.append(bufer.info)
                    if(bufer.next == None): break                     
                    bufer = bufer.next
            i += 1 
        if(arr == []):
            arr.append("Не нашел")       
        return arr 

    def remove_book(self, title):
        i = 0
        while (i < len(self.library)):
            if(title == self.library[i].info):
                bufer = self.library[i]
                while(bufer != None):
                    bufer = self.library[i].next
                    del self.library[i]
                return
            i += 1    


library = Library()
library.add_book("1", "1")
library.add_book("1", "1")
library.add_book("2", "2")
library.add_book("3", "3")
library.add_book("3", "3")
library.add_book("4", "4")

print(library.find_book_by_author('1'))
print(library.find_book_by_title('3'))
print(library.find_book_by_author('2'))

library.remove_book('2')

print(library.find_book_by_author('2'))
