'''def welcome (func):
    def wrapper():
        print("Welcome to PESC Mandya")
        func()
        print("Thank you ,have a nice day!")
    return wrapper

@welcome
def Bhashana():
    print("PESC Mandya had a History of 62 years.Dr Shankaregowda is the founder of PESC Mandya")
Bhashana()
'''
#passing arguments to the decorator
def welcome (func):
    def wrapper(name):
        print("Good Morning")
        func(name)
        print("Have a Nice Day!")
@welcome
def std_name(name):
    print("My name is ",name)
std_name("Ananya B M")


