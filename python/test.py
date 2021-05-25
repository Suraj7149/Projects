import keyword

def identifiers():
    '''program to print the identifiers in the given program.'''

    print('''    A Python identifier can be a combination of lowercase/ uppercase
    letters, digits, or an underscore. The following characters are valid:

    Lowercase letters (a to z)
    Uppercase letters (A to Z)
    Digits (0 to 9)
    Underscore (_)

    Some valid names are:
        myVar
        var_3
        this_works_too

    b. An identifier cannot begin with a digit.
    
    Some valid names:
        _9lives 
        lives9
        
    An invalid name:
        9lives\n''')

def keywords():
    '''to print the keywords of the program.'''
    print("Keywords in python are:- \n")
    for i in keyword.kwlist:
        print(i)
    print(" ")

def literals():
    '''to print the literals in the program.'''
    print('''Generally, literals are a notation for representing a fixed value in source code. 
    They can also be defined as raw value or data given in variables or constants. 

    Example:
    # Numeric literals
    x = 24
    z = 2+3j
    print(x, y, z)
    Output
    24 24.3 (2+3j)
    Here 24, 24.3, 2+3j are considered as literals. 

    Python has different types of literals.

    String literals
    Numeric literals
    Boolean literals
    Literal Collections
    Special literals
    String literals
    A string literal can be created by writing a text(a group of Characters ) surrounded by the 
    single(”), double(“”), or triple quotes.  By using triple quotes we can write multi-line strings 
    or display in the desired way. 

    Example:

    # string literals
  
    # in single quote
    s = 'geekforgeeks'
  
    # in double quotes
    t = "geekforgeeks"
  
    # multi-line String
    m = ''geek 
           for 
               geeks''
  

    Here geekforgeeks is string literal which is assigned to variable(s). 

    Character literal
    It is also a type of string literals where a single character surrounded by single or double-quotes.

    Example:
    # character literal in single quote
    v = 'n'
  
    # character literal in double quotes
    w = "a"
  
    Numeric literals
    They are  immutable and there are three types of numeric literal : 
    Integer
    Float
    Complex.
    Integer :
    Both positive and negative numbers including 0. There should not be any fractional part.

    Example:
    # integer literal
  
    # Binary Literals
    a = 0b10100
  
    # Decimal Literal
    b = 50
  
    # Octal Literal
    c = 0o320
  
    # Hexadecimal Literal
    d = 0x12b
  
    print(a, b, c, d)
    Output
    20 50 208 299
    In the program above we assigned integer literals (0b10100, 50, 0o320, 0x12b) into different 
    variables. Here, ‘a‘ is binary literal, ‘b’ is a decimal literal, ‘c‘ is an octal literal and 
    ‘d‘ is a hexadecimal literal. But on using print function to display value or to get output 
    they were converted into decimal.

    Float
    These are real numbers having both integer and fractional parts.

    Example:
    # Float Literal
    e = 24.8
    f = 45.0

    
    24.8 and 45.0 are floating-point literals because both 24.8 and 45.0 are floating-point numbers.

    Complex Literal 
    The numerals will be in the form of a+bj, where ‘a‘ is the real part and ‘b‘ is the complex part.

    Example:
    z = 7 + 5j
  
    # real part is 0 here.
    k = 7j

    Boolean literals
    There are only two boolean literals in Python. They are true and false.

    Example:

    a = (1 == True)
    b = (1 == False)
    c = True + 3
    d = False + 7
    
    In python, True represents the value as 1 and False represents the value as 0. In the above example 
    ‘a‘ is True and ‘b‘ is False because 1 equal to True.

    Example:
    x = (1 == True) 
    y = (2 == False)
    z = (3 == True)
    r = (1 == True)
    a = True + 10
    b = False + 10
  

    Literal Collections
    There are four different types of literal collections

    List literals
    Tuple literals
    Dict literals
    Set literals
    List literals 
    List contains items of different data types. The values stored in List are separated by comma (,) and 
    enclosed within square brackets([]). We can store different types of data in a List. Lists are mutable.

    Example : 

    # List literals
    number = [1, 2, 3, 4, 5]
    name = ['Amit', 'kabir', 'bhaskar', 2]
    print(number)
    print(name)

    Tuple literals
    A tuple is a collection of different data-type.  It is enclosed by the parentheses ‘()‘ and each element 
    is separated by the comma(,). It is immutable.

    Example: 

    # Tuple literals
    even_number = (2, 4, 6, 8)
    odd_number = (1, 3, 5, 7)
  
    
    Dictionary literals
    Dictionary stores the data in the key-value pair. It is enclosed by curly-braces {} and each pair is 
    separated by the commas(,).  We can store different types of data in a dictionary. Dictionaries are mutable.

    Example: 

    # Dict literals
    alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
    information = {'name': 'amit', 'age': 20, 'ID': 20}
  
    
    Set literals
    Set is the collection of the unordered data set. It is enclosed by the {} and each element is separated by the comma(,).

    Example: we can create a set of vowels and fruits. 

    # Set literals
    vowels = {'a', 'e', 'i', 'o', 'u'}
    fruits = {"apple", "banana", "cherry"}
  
    Special literals
    Python contains one special literal (None). ‘None’ is used to define a null variable. If ‘None’ is compared with 
    anything else other than a ‘None’, it will return false.

    Example:

    # Special literals
    water_remain = None''')

if "__main__" == __name__:
    loop = True
    while(loop):

        choice = input(">>>")

        if choice.lower() == "exit":
            break

        elif choice.lower() == "identifiers":
            identifiers()

        elif choice.lower() == "about program":
            print("cmd based program for demo")

        elif choice.lower() == "keywords":
            keywords()

        elif choice.lower() == "literals":
            literals()

        elif choice.lower() == "about":
            print('Commands:-\n\t- identifiers\n\t- about\n\t- about programe\n\t- keywords\n\t- literals\n\t- exit')
        
        else:
            continue
