'''def first_func(fun) :
    print("First function") #1
    return fun #2

def second_fun() :
    print("Second function") #4

def function_caller(fun) :
    fun() #3

#function_caller(first_func(second_fun))

x = first_func(second_fun)
x()

def decorator(func) :
    print("Decorator line 1") #1
    func()
    print("Decorator line 2") #3

@decorator
def hello():
    print("Hello") #2

#hello = decorator(hello)

hello()'''


def hello_decorator(func):

    def inner1():
        print("Hello, this is before function execution") #2
        func() #3
        print("This is after function execution") #5
         
    return inner1

@hello_decorator
def function_to_be_used():
    print("This is inside the function !!") #4

function_to_be_used() #1

#function_to_be_used = hello_decorator(function_to_be_used)
#@hello_decorator

'''
import time
import math

#func = factorial
def calculate_time(func):
	
	def inner1(*args, **kwargs):

		begin = time.time() #1
		#factorial(*args, **kwargs)
		func(*args, **kwargs)

		end = time.time() #4
		print("Total time taken in : ", func.__name__, end - begin) #5

	return inner1

#factorial = calculate_time(factorial)
#factorial = inner1
@calculate_time
def factorial(num):
	time.sleep(2) #2
	print(math.factorial(num)) #3

# calling the function.
#inner1(10)
factorial(10)
'''

def decor1(func):
    def inner(): #2ndinner
        x = func() #inner in decor #2
        # x = 20
        return x * x #6
    return inner

def decor(func):
    def inner(): #1stinner
        x = func() #num #3
        # x = 10
        return 2 * x #5
    return inner
 
@decor1
@decor
def num():
    return 10 #4

#num = decor1(decor(num))
#num = decor1(1stinner)
#num = 2ndinner

#print(2ndinner())
print(num()) #1
'''
inner2()
    x = inner1()
        x = num()
            return 10
        return 2 * x
    return x * x
'''

