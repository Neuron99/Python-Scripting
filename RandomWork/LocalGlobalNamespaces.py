"""
builtin scopes : this is where all the builtin methods are stored.
global scope :module namespace 
local scope : function namespace
nonlocal scope : neither local nor global, this is applicable only when there is nested functions.

"""
c = 100 #this is the global variable
a = 10 #this is the global variable
def method_(a,b):
    return a,b,c
"""
local namespace is detected while compiling the function.
global namespace is referenced during the runtime if the variable is not in the local namespace.
"""
method_(1,0) #this will print the local variables and global variable if it is not found in the local namespace


def method2(a,b):
    c = 0.33 # this is the local variable and this is identified during the compilation time.
    return a,b,c
method2(4,6)  # this will return the c in local namespace

def method3(a,b):
    global c
    return a,b,c

method3(10,20) # this will return tuple containing local a and b and global c


"""
it is not necessary to create a global variable before using it in the local namespace with the global keyword.
all the local variable references are removed from the local namespace after the execution of the function.

"""

def method4(a,b):
    global z
    z = 2000
    return a,b,z

method4(10,50)
print(z) #this will return the value of z

#-----------------------------------------------------------------------------------------------
#nested functions and nonlocalscope 

def outer():
    a = 10 # a is the local to outer function
    print("local space of outer method :",a)
    def inner():
        a = 30
        print("this is local namespace of inner method :",a)
    inner()
outer()    

#accessing and modifying the local space of other method or function using nonlocal keyword.
def outer():
    """this is nonlocal space of other method"""
    a = 10 # a is the local to outer function
    print("local space of outer method :",a)
    def inner():
        """nonlocal space of outer method"""
        nonlocal a
        a = 20
        print("a from the nonlocalspace :",a)
    inner()
    print("after modifying the a value:",a)
outer()