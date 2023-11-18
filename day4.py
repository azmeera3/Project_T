

#best practise for above case
#with help of functions advantages: reusability, readability, debugging.

a=2
b=3

def addition():                    #function_1    { def is a(keyword) = defination or function;{def addition ():}"def" "name of the function" "()":}
    add = a + b
    print(add) #print("value of addition", addition) #+ str(addition))

def sub():                         #function_2
    sub = a - b 
    print(sub)

def multiplication():                         #function_3
    m = a * b
    print(m)

addition()              # we need to call with function name in the end
sub()                   #we need to invoke them or else python will exit the code
multiplication()        # in case of main function there is no need to invoke/no need to call


#Functions : functions takes input and returns
#
def addition(a, b):  #return input
    add = a + b
    return add   #return will help in returing the variable value and helps in repacing them

print(addition(5, 10))
#

# MODULE : group of functions / collection of function / set of config file{poorna}
#          to use the module in another module we use import 
#          MODULES are used for re-usability, by using import function.


# Packages : collection of modules { collection of 1k files for a micro-services is called a package/library}

# PYPI : Python Package Index is artifactory/repository to store python related modules 

# PIP : we can install anything within pip by using it . "PIP install BOTO-3"

# VIRTUAL ENVOIRMENT : usefull when using same machine for different projects.
#                      it will do a logical separation for the python packages.
# "python -m venv Project -abc"                     "Python -m venv{command}" "Project -abc{project_name}" 
#

