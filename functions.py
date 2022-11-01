# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
from xmlrpc.client import boolean

def greet (x):
    zin = ("Hello, "+ str(x + '!'))
    print (zin)
    return (zin)

def add (x, y, z):
    total = float(x + y + z)
    print (total)
    return (total)

def positive(x):
    if x > 0:
        return (True) 
    if x == 0:
        return (False)
    if x < 0:
        return (False)

def negative(x):
    if x > 0:
        return (False) 
    if x < 0:
        return (True)
    if x == 0:
        return (False)

greet("Bob")
add(5, 3, 2)
positive(50)
positive(-50)
positive(0)
negative(50)
negative(-50)
negative(0)
