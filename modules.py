# own modules
# thirdy party modules
# python modules

# import datetime

# print(datetime.date.today())

# print(datetime.timedelta(minutes=100))

# from datetime import timedelta, date

# print(date.today())

# import mymathmodule

# mymathmodule.add(1,2)

# mymathmodule.substract(1,2)

# from mymathmodule import add, substract

# substract(1,2)
# add(1,2)

from lib2to3.pytree import convert
from colorama import Fore, Style, init

init(convert=True) 
print(Fore.RED +"hello world")
