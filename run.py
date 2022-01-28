def a(b):

    def c():
        print("abc")
        return b()

    return c
@a

def display():
    i += 1
    print("hee")

i = 0
display() 
