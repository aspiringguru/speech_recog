#https://pypi.org/project/semantic/
##create virtual env for package installation
#virtualenv semanticenv
##deactivate the existing virtual env
##activate the virtual env
#semanticenv\Scripts\activate


#pip install semantic

from semantic.dates import DateService

from semantic.dates import DateService

service = DateService()
date = service.extractDate("On March 3 at 12:15pm...")

#---------------------------------------------------
#this fails
# from semantic.solver import ConversionService
# service = ConversionService()
# print (service.convert("Seven and a half kilograms to pounds"))
# print (service.convert("Seven and a half pounds per square foot to kilograms per meter squared"))


#--------------
from semantic.numbers import NumberService
service = NumberService()
print (service.parse("Two hundred and six"))
# 206
print (service.parse("Five point one five"))
# 5.15
print (service.parse("Eleven and two thirds"))
# 11.666666666666666
print (service.parseMagnitude("7e-05"))
#--------------
#from semantic.solver import MathService
#service = MathService()
#print (service.parseEquation("Log one hundred and ten"))
