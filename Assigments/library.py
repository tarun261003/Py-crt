import time
class Library:
    def __init__(self,name,book_list):
        self.name=name
        self.book_list=book_list
    def add_book(self,book_title):
        if book_title not in self.book_list:
            self.book_list.append(book_title)
            return "Book added"
        return "Already Exists"
    def remove_book(self,book_title):
        try:
            self.book_list.remove(book_title)
            return "Done! removed!"
        except Exception as e:
            return "Not Found"
    def listBooks(self):
        return self.book_list
    def search_book(self,book_list):
         return book_list in self.book_list
    def display_information(self):
        return f"This library name is {self.name} and it consists of {len(self.book_list)} books."
def print_slow(text,delay=0.03):
    for char in text:
        print(char,end='')
        time.sleep(delay)
    print()
book_names = ["The Shadow Thief", "The Lampo Circus", "Von Gobstopper's Arcade", "Halo", "Hades", "Blackkerchief Dick", "The Country of Carnival", "Village 1104", "The Young Visiters", "The Life of Father McSwiney", "In the Forests of the Night", "Demon in My View", "Shattered Mirror", "Midnight Predator", "Hawksong", "Snakecharm", "Lady Susan", "The Room on the Roof", "The Viper of Milan", "Gabriel Denver", "The Swish of the Curtain", "Sir Quixote of the Moors", "The Lost Princess", "The Prophecy of the Stones", "Fugitive Pieces", "Hours of Idleness", "The Romance of Atlantis", "Kiffe kiffe demain", "The Brown Owl", "The Feather", "The Shifting of the Fire", "The Diary of a Young Girl", "My Brilliant Career", "These Violent Delights", "How to Talk to Girls", "The DUFF", "The Three Adventurers at Fungalore", "Crazy", "The Monk", "Looking Back", "Lost Laysen", "Flowers and Shadows", "Solitaire", "The Icarus Girl", "Eragon", "How the World Began", "Sharh Al-Isti'aadha wal-Basmalah", "The Broken Melody", "The Neon Bible", "True Spirit", "The Loom of Youth", "Mirror Dreams", "Mirror Wakes", "Waywalkers", "Timekeepers", "The Extraordinary and Unusual Adventures of Horatio Lyle", "Swordbird", "Sword Quest", "Sword Mountain", "What's Left of Me"]
cse_books = ["Introduction to Algorithms", "The C Programming Language", "The Pragmatic Programmer", "The Art of Computer Programming", "Structure and Interpretation of Computer Programs", "The Mythical Man-Month", "Design patterns", "Clean Code", "Code", "Operating systems", "Purely functional data structures", "Software design for flexibility", "Computer Organization and Design: The Hardware/software Interface", "Discrete Mathematics and Its Applications", "Python programming", "Theory of computation", "AI and humanity", "Foundations of Computer Science", "How the Mind Works?", "Intro to CS book", "Mathematical foundations of data science", "Network programming", "Programming Language Design and Implementation", "Computational thinking"]
ece_books = ["Signals and Systems", "Analogue electronics", "Microe   lectronic Circuits", "Linear ICs", "Engineering Mathematics", "Network theory", "Semiconductor device", "Complex analysis", "Control system", "Control Systems Engineering", "Differential equation", "Digital electronics", "Electrical m", "Electronic circuits", "Linear algebra", "Microprocessors and microcontrollers", "Numerical analysis", "Electronic Devices and Circuit Theory", "Antenna theory by Balanis", "Digital Signal Processing by sk Mitra", "Network Analysis by Van Valkenburg", "CO", "Digital circuits by anand kumar", "Fundamentals of digital SY"]
gen=Library('Stroy Library',book_names)
cse=Library('CSE',cse_books)
ece=Library('ECE',ece_books)
print_slow('Welcome!...')
print('1.story\n2.cse\n3.ece\n')
ch=int(input('Enter the library you want to enter:'))
if ch==1:
    print_slow('Taking you to story library')
    print('1.Add\n2.Remove\n3.ListBooks\n4.Search\n5.Display')
    while True:
        ch1=int(input('Enter your choice:'))
        if ch1==1:
            print(gen.add_book(input('Enter the book title:')))
        elif ch1==2:
            print(gen.remove_book(input('Enter the book title:')))
        elif ch1==3:
            for i in gen.listBooks():
                print(i)
        elif ch1==4:
            temp="👍" if gen.search_book(input('Enter the book title:')) else "😒"
            print(temp)
        elif ch1==5:
            print(gen.display_information())
        else:
            print('Exiting..')
            exit()
elif ch==2:
    print_slow('Taking you to CSE library')
    print('1.Add\n2.Remove\n3.ListBooks\n4.Search\n5.Display')
    while True:
        ch1=int(input('Enter your choice:'))
        if ch1==1:
            print(cse.add_book(input('Enter the book title:')))
        elif ch1==2:
            print(cse.remove_book(input('Enter the book title:')))
        elif ch1==3:
            for i in cse.listBooks():
                print(i)
        elif ch1==4:
            temp="👍" if cse.search_book(input('Enter the book title:')) else "😒"
            print(temp)
        elif ch1==5:
            print(cse.display_information())
        else:
            print('Exiting..')
            exit()
elif ch==3:
    print_slow('Taking you to ECE library')
    print('1.Add\n2.Remove\n3.ListBooks\n4.Search\n5.Display')
    while True:
        ch1=int(input('Enter your choice:'))
        if ch1==1:
            print(ece.add_book(input('Enter the book title:')))
        elif ch1==2:
            print(ece.remove_book(input('Enter the book title:')))
        elif ch1==3:
            for i in ece.listBooks():
                print(i)
        elif ch1==4:
            temp="👍" if ece.search_book(input('Enter the book title:')) else "😒"
            print(temp)
        elif ch1==5:
            print(ece.display_information())
        else:
            print_slow('Exiting..')
            exit()
else:
    print('Enter valid one!')