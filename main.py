##############################################################################

# Hello World

##############################################################################
'''
print("Hello World")
'''
##############################################################################

# Wprowadzanie danych

##############################################################################
def introduction_data():
    data = input("Podaj swoje imie, nazwisko i rok urodzenia: ")
    data = data.split()

    name = data[0]
    surname = data[1]
    birthYear = data[2]

    print("Witaj " + name + " " + surname + " urodzony w " +birthYear+ "!")
###############################################################################

# Zapis danych

##############################################################################
def save_data():
 kod = 1234

 while(1):
 password = int(input("PASSWORD: "))

 if(kod == password):
 print("Welcome in!!!")
 break
 else /* : */
 print("Try again!")
##############################################################################

# Ilosc plikow

##############################################################################
def number_of_file():
    import os
    path = 'D:\Nazwa pliku\Nazwa pliku\Nazwa pliku'           #tutaj wpisujemy swoją ścieżkę do katalogu
    files = os.listdir(path)
    print("W pliku o ścieżce " + path + " znajduje sie " + str(len(files)) + " pliki")
##############################################################################

# Struktura katalogu

##############################################################################
def directory_structure():
    import os

    path = 'D:\Nazwa pliku\Nazwa pliku\Nazwa pliku'           #tutaj wpisujemy swoją ścieżkę do katalogu
    end_path = 'D:\ '                                         #koniec wypisywania zawartości plików

    while path != end_path[:-1]:
        print(path)
        print('\n'.join(os.listdir(path)))
        path = os.path.dirname(path)
        print('\n')

    print(path)
    print('\n'.join(os.listdir(path)))
##############################################################################

# Konwersja rozszerzenia 

##############################################################################
def conversion_extension():
import os
from PIL import Image
path = 'D:\Nazwa pliku\Nazwa pliku'           #tutaj wpisujemy ścieżke do katalogu ze zdjęciami
files = os.listdir(path)
for f in files:
    im = Image.open(path)
    im.convert('RGB').save(path+"/"+f.split(".")[0]+".png","PNG")
##############################################################################

# Usuwanie slow

##############################################################################
def delete_words():
    text = ''''''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 
    eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim 
    veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur.Excepteur sint occaecat cupidatat
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.''''''
    
    text = text.split()
    wordToDelete = 'in'
    textToRead = ''

    for i in range(text.count(wordToDelete)):
        text.remove(wordToDelete)
    
    for word  in text:
        textToRead += word + ' '
    
    print(textToRead)
##############################################################################

# Podmienianie slow

##############################################################################
def replace_words():
    text = ''''''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 
    eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim 
    veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur.Excepteur sint occaecat cupidatat
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.''''''
    
    text = text.split()
    changingDictionary = {'in' : '1', 'Lorem' : '0', 'laborum' : '100'} 
    textToRead = ''

    for words in changingDictionary:
        for texts in text:
            if(words == texts):
                for i in range(text.count(texts)):
                    index = text.index(texts)
                    text.insert(index, changingDictionary[texts])
                    text.remove(texts)
                

    for word  in text:
        textToRead = textToRead + word + ' '
    
    print(textToRead)
##############################################################################

# Równanie kwadratowe

##############################################################################
'''
import math
print ("Rownanie kwardatowe ax^2+bx+c")
a = int(input("Podaj wspolczynnik rowniania a: "))
b = int(input("Podaj wspolczynnik rowniania b: "))
c = int(input("Podaj wspolczynnik rowniania c: "))

if a == b == c == 0:
    print ("a, b, c = 0 - Rownanie o nieskonczonej ilosci rozwiazan")
else:
    delta = b*b-(4*a*c)
    print ("Delta: " + str(delta))
    from math import sqrt
    sqrt_delta = int(sqrt(delta))
    print(str(sqrt_delta))
    if delta < 0:
        print ("Delta< 0 brak pierwiastkow.")
    else:
        x1=(-b-sqrt_delta)/(2*a)
        x2=(-b+sqrt_delta)/(2*a)
        print ("X1 = " + str(x1) + ", X2 = " + str(x2))
'''
##############################################################################

# Sortowanie

##############################################################################
'''
import random

tab = random.sample(range(100000),50)
in_tab = tab[:]
in_tab2 = tab[:]

for x in range(len(in_tab)):
    for y in range(len(in_tab)):
        if x != y and in_tab[x] < in_tab[y]:
            tmp = in_tab[y]
            in_tab[y] = in_tab[x]
            in_tab[x] = tmp

if in_tab == sorted(in_tab2):
    print("Liczby są dobrze posortowane")
else:
    print("Spróbuj jeszcze raz") 
'''
##############################################################################

# Iloczyn skalarny

##############################################################################
'''
def dot_product(a, b):
    """Counting dot product of two 1D lists of the same size
    Input:
    a, b - lists with int values, len(a) == len(b)!!!
    Output:
    None, if lists aren't the same size or counted dot product
    """
    
    if len(a) != len(b):
        print("lists aren't the same size")
        return None
    else:
        return sum([a[index] * b[index] for index in range(len(a))])
a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
dot_product(a, b)
'''
##############################################################################

# Suma macierzy

##############################################################################
'''
def matrix_adder(matrix1, matrix2):    
    try:
        
        x = []
        for row in range(len(matrix1)):
            x.append([matrix1[row][index] + matrix2[row][index]
                      for index in range(len(matrix1[row]))])
        return x
    
    except:
        print("Matrixes are differ in size or values aren't numeric")
        

a = [[1,2],[3,4]]
b = [[-1,-2],[-3,-4]]
matrix_adder(a,b)
'''

##############################################################################

# Mnożenie macierzy

##############################################################################
'''
import numpy as np

A = np.array([[3,4,5], [1,2,3], [4,5,6]])
B = np.array([[-2, 5,1], [7, 0, 2], [-1, 0,5]])

C = A*B
print(str(C))
'''
##############################################################################

# Wyznacznik macierzy

##############################################################################
'''
import numpy as np

A = np.array([[3,-50,4,5], [1,2,12,3], [4,5,6,59], [423,-5,36,29]])

print("wyznacznik macierzy to: " + str(np.linalg.det(A)))
'''

##############################################################################

# Complex numbers

##############################################################################
'''

class MyComplex:
    def __init__(self, number):
        if __title(number) == complex:
            self.real = number.real
            self.imag = number.imag
        elif __title(number) == MyComplex:
            self.real = number.get_real()
            self.imag = number.get_imag()

    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imag

    def __add__(self, number):
        if __title(number) == complex:
            a = self.get_real() + number.real
            b = self.get_imag() + number.imag
            return str(str(a) + " + j" + str(b))
        elif __title(number) == MyComplex:
            a = self.get_real() + number.get_real()
            b = self.get_imag() + number.get_imag()
            return str(str(a) + " + j" + str(b))

    def __sub__(self, number):
        if __title(number) == complex:
            a = self.get_real() - number.real
            b = self.get_imag() + number.imag
            return str(str(a) + str(complex(0, b)))
        elif __title(number) == MyComplex:
            a = self.get_real() - number.get_real()
            b = self.get_imag() + number.get_imag()
            return str(str(int(a)) + ('+' if b > 0 else '+') + str(complex(0, b)))

    def __mul__(self, number):
        if __title(number) == complex:
            a = self.get_real() * number.real - self.get_imag() * number.imag
            b = self.get_imag() * number.real + self.get_real() * number.imag
            return str(str(a) + " + j" + str(b))
        elif __title(number) == MyComplex:
            a = self.get_real() * number.get_real() - self.get_imag() * number.get_imag()
            b = self.get_real() * number.get_imag() + self.get_imag() * number.get_real()
            return str(str(a) + " + j" + str(b))

    def __mod__(self):
        a = pow((pow(self.get_real()) + pow(self.real)), 0.5)
        return str(str(a))

    def __str__(self):
        a = self.real + self.imag * complex(0, 1)
        return str(a)

    def compute(self, to_compute):
        self = MyComplex(complex(int(to_compute[0] + to_compute[1]), int(to_compute[2] + to_compute[4])))
        other = MyComplex(complex(int('+' + to_compute[6]), int(to_compute[7] + to_compute[9])))
        complex_result = 0
        if to_compute[5] == "+":
            complex_result = self + other
        elif to_compute[5] == "-":
            complex_result = self - other
        elif to_compute[5] == "*":
            complex_result = self * other
        elif to_compute[5] == "||":
            complex_result = self.get_real() + self.get_imag()
        print(complex_result)


obj3 = MyComplex(1 + 4j)
obj4 = MyComplex(9 + 8j)
obj5 = obj3 + obj4


# print(obj5)
'''
##############################################################################

# Calculator

##############################################################################
'''
class Calculate:
    @staticmethod
    def __add(one, other):
        return one + other

    @staticmethod
    def __sub(one, other):
        return one - other

    @staticmethod
    def __mul(one, other):
        return one * other

    @staticmethod
    def __truediv(one, other):
        return one / other

    def __floordiv(self, one, other):
        return int(self.__truediv(one, other))

    def __mod(self, one, other):
        return one - self.__floordiv(self, one, other) * other

    @staticmethod
    def __pow(one, other):
        if other == 0:
            return 1
        elif other == 1:
            return one
        a = one
        for i in range(1, other):
            one = one * a
        return one

    def compute(self, calculator: object, to_compute: object) -> object:
        to_compute = to_compute.split()
        if 'j' in to_compute:
            return calculator.compute(calculator, to_compute)
        else:
            a = int(to_compute[0])
            b = int(to_compute[2])
            if to_compute[1] == "+":
                result = self.__add(a, b)
            elif to_compute[1] == "-":
                result = self.__sub(a, b)
            elif to_compute[1] == "*":
                result = self.__mul(a, b)
            elif to_compute[1] == "/":
                result = self.__truediv(a, b)
            elif to_compute[1] == "int/":
                result = self.__floordiv(a, b)
            elif to_compute[1] == "||":
                result = self.__mod(a, b)
            elif to_compute[1] == "^":
                result = self.__pow(a, b)

        print(str(result))


obj = Calculate
obj1 = MyComplex
obj.compute(obj, obj1, "+ 10 + j 3 + 7 - j 5")
'''


########################################################################################################################
#
# XML
#
########################################################################################################################

def sax_parsing():
    print("sax parsing")

    import xml.sax

    class MovieHandler(xml.sax.ContentHandler):
        def __init__(self):
            self.__database = ""
            self.__title = ""
            self.__genre = ""
            self.__year = ""
            self.__grade = ""

        def startElement(self, tag, attributes):
            self.__database = tag
            if tag == "movie":
                title = attributes["title"]
                print("Title: " + title)

        def endElement(self, tag):
            if self.__database == "title":
                print("Type:" + self.__title)
            elif self.__database == "genre":
                print("Format:" + self.__genre)
            elif self.__database == "year":
                print("Year:" + self.__year)
            elif self.__database == "grade":
                print("Rating:" + self.__grade)
            self.__database = ""

        def characters(self, content):
            if self.__database == "title":
                self.__title = content
            elif self.__database == "genre":
                self.__genre = content
            elif self.__database == "year":
                self.__year = content
            elif self.__database == "grade":
                self.__grade = content

    if __name__ == "__main__":
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        parser.setContentHandler(MovieHandler())

        parser.parse("database.xml")


def dom_parsing():
    print("dom parsing")

    from xml.dom import minidom
    import random

    database = minidom.parse("database.xml")
    collection = database.documentElement
    if collection.hasAttribute("shelf"):
        print("Root element : %s" % collection.getAttribute("shelf"))

    movies = collection.getElementsByTagName("movie")

    for movie in movies:
        print("Title: %s" % movie.getAttribute("title"))
        if movie.getElementsByTagName('genre'):
            genre = movie.getElementsByTagName('genre')[0]
            print("Genre: %s" % genre.childNodes[0].data)
        if movie.getElementsByTagName('year'):
            year = movie.getElementsByTagName('year')[0]
            print("Year: %s" % year.childNodes[0].data)
        if movie.getElementsByTagName('grade'):
            grade = movie.getElementsByTagName('grade')[0]
            print("Grade: %s" % grade.childNodes[0].data)
           
    for mov in movies:
        mov.setAttribute('title', str(random.randint(0,10)))
        mov.setAttribute('shelf', str('Old'))
    database.writexml(open('new_database.xml', 'w'))
    
sax_parsing()
dom_parsing()
########################################################################################################################
#
# CSV/JSON
#
########################################################################################################################
'''
import json
from pathlib import Path

word_lenght = 16


class Program:
    def __init__(self):
        my_file = Path('database.json')
        if my_file.is_file():
            self.__database = list()
            self.open()
            self.work()
        else:
            print('You do not have database file. Reinstall is needed!')

    def open(self):
        with open('database.json', 'r') as file:
            try:
                self.__database = json.load(file)
            except:
                print('You have an empty library! Add some movies!')
                self.add_data()

    def save(self):
        with open('database.json', 'w') as f:
            json.dump(self.__database, f, sort_keys=True, indent=4)

    def read(self):
        print('Your movie base:\n||Title           ||Genre           ||Year of premiere||Grade (0- 10)   ||')
        for dict_element in self.__database:
            to_print = "||" + str(dict_element["Title: "])
            to_print += "||" + str(dict_element["Genre: "])
            to_print += "||" + str(dict_element["Year of premiere: "])
            to_print += "||" + str(dict_element["Grade (0 - 10): "])
            to_print += "||"
            print(to_print)

    def add_data(self):
        decision = 'Y'
        movie_dict = {}
        while decision == 'Y' or decision == 'y':
            title = input('Title: ').ljust(word_lenght)[:word_lenght]
            genre = input('Genre: ').ljust(word_lenght)[:word_lenght]
            __year = input('Year of premiere: ').ljust(word_lenght)[:word_lenght]
            grade = input('Grade (0 - 10): ').ljust(word_lenght)[:word_lenght]
            movie_dict = {'Title: ': title, 'Genre: ': genre, 'Year of premiere: ': __year,
                          'Grade (0 - 10): ': grade}
            decision = input('Would You like to add another one?(Y/n):')
            self.__database.append(movie_dict)
            self.save()

    def work(self):
        self.read()
        choice = input("\n\n1- add new\n2- delete one")
        if choice == str(1):
            self.add_data()
        else:
            self.delete_data()

    def delete_data(self):
        done = False
        while not done:
            choice = input("Which title You want to delete: ").ljust(word_lenght)[:word_lenght]
            for dict_element in self.__database:
                if dict_element["Title: "] == choice:
                    self.__database.remove(dict_element)
                    done = True
            if not done:
                print("No movie has this title. So again:")
        self.save()


obj = Program()
obj.open()
while 1:
    obj.work()
'''
########################################################################################################################

#inttroduction_data()
#save_data()
#number_of_file()
#directory_structure()
#conversion_extension():
#delete_words()
#replace_words()
