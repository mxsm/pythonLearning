from com.github.mxsm.ClassObject import MyClass

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


count = 0
def global_test():
    print(count)



def global_counter():
    global count
    count += 1
    return count

def global_counter_test():
    print(global_counter())
    print(global_counter())
    print(global_counter())

global_test()
global_counter_test()
x = MyClass()
xx = x.f
print(x.f())
print(xx())
print(MyClass.f.__name__)

