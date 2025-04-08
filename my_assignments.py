# 🧠 Efe's Custom Python Questions & Answers for 1on1

# 1. Print your favorite hobby on the screen
print("My favorite hobby is playing guitar")

# 2. Create a variable called 'city' and assign it a string value, then print it
city = "Istanbul"
print(city)

# 3. Create a variable called 'height' (in cm), display its type, and convert it to float
height = 175
print(type(height))        # int
height = float(height)
print(type(height))        # float

# 4. Write an if-else statement: check if a number is even or odd
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 5. Create a list of your 3 favorite songs, then add one more using append()
songs = ["Blinding Lights", "Bohemian Rhapsody", "Lose Yourself"]
songs.append("Smells Like Teen Spirit")
print(songs)

# 6. Create a for loop that prints all characters in your name
name = "Efe"
for char in name:
    print(char)

# 7. Create a dictionary for a book (title, author, pages), then print the title
book = {
    "title": "1984",
    "author": "George Orwell",
    "pages": 328
}
print("Book title:", book["title"])

# 8. Create a class called Car with brand and year, and print its info using a method
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

my_car = Car("BMW", 2020)
my_car.show_info()
