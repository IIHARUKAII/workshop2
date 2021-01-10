x = "awesome"


def myfunc():
    global x
    # print(x = "awesome")
    print("Python is " + x)
    x = "fantastic"
    # print(x = "fantastic")


myfunc()
print("Python is " + x)