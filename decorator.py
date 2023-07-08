def greet(fx): 
    def mfx(*args,**kwargs): 
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thank for using this function")
    return mfx

@greet #greet(hello())
def hello(): 
    print("Hello Nigga's")

@greet
def add(a,b): 
    print(a+b)

hello()
greet(add(2,4))

    


