#repeat a set of operation with a set of parameters

def SquareIt(x):
    return x * x
print SquareIt(2)

def DoSomething(f,x):
    return f(x)

print DoSomething(SquareIt, 3)

print DoSomething(lambda x: x*x*x, 3)
#Lambda let you inline simple fuctions
#Make a transitori function that will only work here
