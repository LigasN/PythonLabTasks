##############################################################################

#Hello World

##############################################################################

#print("Hello World")

##############################################################################

#Wprowadzanie danych

##############################################################################

#data = input("Podaj swoje imie, nazwisko i rok urodzenia: ")
#data = data.split()
#
#name = data[0]
#surname = data[1]
#birthYear = data[2]
#
#print("Witaj " + name + " " + surname + " urodzony w " +birthYear+ "!")

###############################################################################


#Zapis danych

##############################################################################
#kod = 1234
#
#while(1):
#password = int(input("PASSWORD: "))
#
#if(kod == password):
#print("Welcome in!!!")
#break
#else /* : */
#print("Try again!")
#
##############################################################################

#Ilosc plikow

##############################################################################
'''
import os.py

DIR = ' C:\ProgramFiles \ Common Files \ System '

a = "C:\ "
b = a[:3]

path, file = os.path.split(DIR)
print(path)
print(file)

while path != b:
    print(DIR)
    ls = os.listdir(DIR)
    path, file = os.path.split(DIR)
    for x in ls:
        print(x)
    DIR(path)
    
ls = os.listdir(DIR)
for x in ls:
    print(x)
'''
##############################################################################

#Usuwanie slow

##############################################################################
'''
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
 '''
##############################################################################

#Podmienianie slow

##############################################################################
'''
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
'''
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
import random, time

def my_sort(ls):
    """Function to sort in decreasing order
    as input enter a list with unsorted numbers
    
    function return None, but its working on reference to
    a list, so te original will change
    """
    
    tmp = None
    cond = True
    
    while cond == True:                         #sorting until proper order (if condition
                                                #always False after looking whole list)
        cond = False
        
        for index in range(1, len(ls)):            
            if ls[index] > ls[index - 1]:
                tmp = ls[index - 1]
                ls[index - 1] = ls[index]
                ls[index] = tmp
                
                cond = True

to_sort = [int(random.random() * 100) for x in range(50)] #list to sort
to_my_sort = to_sort[:]  #copy for another algorithm
start = time.time()     #time check
my_sort(to_my_sort)
my_alg = time.time()
to_sort.sort(reverse = True)
python_alg = time.time()
print('is result the same? ', to_sort == to_my_sort)
print('my_time: ' + str(my_alg - start) + ', python alg time: ' + str(python_alg - my_alg))
'''
##############################################################################

#Iloczyn skalarny

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

#Suma macierzy

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

#Mnożenie macierzy

##############################################################################
'''
import numpy as np

A = np.array([[3,4,5], [1,2,3], [4,5,6]])
B = np.array([[-2, 5,1], [7, 0, 2], [-1, 0,5]])

C = A*B
print(str(C))
'''
##############################################################################

#Wyznacznik macierzy

##############################################################################
'''
import numpy as np

A = np.array([[3,-50,4,5], [1,2,12,3], [4,5,6,59], [423,-5,36,29]])

print("wyznacznik macierzy to: " + str(np.linalg.det(A)))
'''
##############################################################################

#Liczby zespolone

##############################################################################
import math
class myComplex:
    def __init__(self, number):
        if(type(number) == complex):
            self.real = number.real
            self.imag = number.imag
        elif(type(number) == myComplex):
            self.real = number.getReal()
            self.imag = number.getImag()

    def getReal(self):
        return self.real

    def getImag(self):
        return self.imag

    def __add__(self, number):
        if(type(number) == complex):
            a = self.getReal() + number.real
            b = self.getImag() + number.imag
            return str(str(a) + " + j" + str(b))
        elif(type(number) == myComplex):
            a = self.getReal() + number.getReal()
            b = self.getImag() + number.getImag()
            return str(str(a) + " + j" + str(b))

    def __sub__(self, number):
        if(type(number) == complex):
            a = self.getReal() - number.real
            b = self.getImag() - number.imag
            return str(str(a) + " + j" + str(b))
        elif(type(number) == myComplex):
            a = self.getReal() - number.getReal()
            b = self.getImag() - number.getImag()
            return str(str(a) + " + j" + str(b))

    def __mul__(self, number):
        if(type(number) == complex):
            a = self.getReal() * number.real - self.getImag() * number.imag
            b = self.getImag() * number.real + self.getReal() * number.imag
            return str(str(a) + " + j" + str(b))
        elif(type(number) == myComplex):
            a = self.getReal() * number.getReal() - self.getImag() * number.getImag()
            b = self.getReal() * number.getImag() + self.getImag() * number.getReal()
            return str(str(a) + " + j" + str(b))

    def __mod__(self):
        a = sqrt(pow(self.getReal()) + pow(self.real))
        return str(str(a))
    
    def __str__(self):
        a = self.real + self.imag * j;
        return str(a)

    def compute(self, toCompute):
        self = myComplex(complex(int(toCompute[0]),int(toCompute[3])))
        other = myComplex(complex(int(toCompute[5]),int(toCompute[8])))
        if(toCompute[1] == "+"):
            wynik = self + other
        elif(toCompute[1] == "-"):
            wynik = self - other
        elif(toCompute[1] == "*"):
            wynik = self * other
        elif(toCompute[1] == "||"):
            wynik = self
        print(wynik)
        
        

obj3 = myComplex(1+4j)
obj4 = myComplex(9+8j)
obj5 = obj3 + obj4
#print(obj5)

##############################################################################

# Kalkulator Wykorzystaj powyzszą klasę do stworzenia prostego kalkulatora, parsującego i wykonującego równanie podane przez użytkownika

##############################################################################

class Calc:
    def __add(one, other):
        return one + other
    def __sub(one, other):
        return one - other
    def __mul(one, other):
        return one * other
    def	__truediv(one, other):
        return one / other
    def __floordiv(one, other):
        return int(__truediv(other))
    def __mod(one, other):
        return one - __floordiv(other) * other
    def __pow(one, other):
        if (other == 0):
            return 1
        elif (other == 1):
            return one
        a = one
        for i in range(1, other):
            one = one*a
        return one
    def compute(self, obj, toCompute):
        toCompute = toCompute.split()
        print(toCompute)
        if(toCompute[2] == 'j'):
            return obj.compute(obj, toCompute)
        else:
            a = int(toCompute[0])
            b = int(toCompute[2])
            if(toCompute[1] == "+"):
                wynik = self.__add(a, b)
            elif(toCompute[1] == "-"):
                wynik = self.__sub(a, b)
            elif(toCompute[1] == "*"):
                wynik = self.__mul(a, b)
            elif(toCompute[1] == "/"):
                wynik = self.__truediv(a, b)
            elif(toCompute[1] == "int/"):
                wynik = self.__floordiv(a, b)
            elif(toCompute[1] == "||"):
                wynik = self.__mod(a, b)
            elif(toCompute[1] == "^"):
                wynik = self.__pow(a, b)
                    
        print(str(wynik))

obj = Calc
obj1 = myComplex
obj.compute(obj, obj1, "10 + j 3 - 7 - j 5")

    



















