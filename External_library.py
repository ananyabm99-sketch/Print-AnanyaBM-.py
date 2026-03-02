#pypi.org
from currency_converter import CurrencyConverter
from datetime import date
c = CurrencyConverter()
print(c.convert(1000000,"USD","INR"))
print(c.convert(1000000,"USD","INR",date = date(2025,2,25)))
print(c.convert(1,"EUR","INR"))
print(c.convert(1,"EUR","INR",date = date(2025,2,25)))
print(c.convert(1,"INR","EUR"))
print(c.convert(1,"INR","EUR",date = date(2025,2,25)))
print(c.convert(1,"INR","USD"))
print(c.convert(1,"INR","USD",date = date(2025,2,25)))