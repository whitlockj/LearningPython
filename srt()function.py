from types import FunctionType


#str() FunctionType
# can be useful if you have an string sentence 
# and you have an integer
# (number) and you want to print 
# them together as an string to be in one sentense

Myname= "Hello my name is Jeff and my age is"
age=32
total=(Myname + age)
print=(total)

## will give an error line 12. This is because theres
#a veriable and a string. With no str() function
#Fix:


Myname= "Hello my name is Jeff and my age is"
age=32
total=(Myname + str(age))
print=(total)

## will be: Hello my name is jeff and my age is 32

