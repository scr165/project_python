print("Please enter your firstnumber")
a=float(input(">"))
print("Please enter another number")
b=float(input(">"))
dec=input( "if you want addition press '1'\nif you want subtraction press '2'\nif you wanr multiplication press '3'\nif you want division press '4'\n")

def addition(a,b):
    print('the result is',a+b)
def subtraction(a,b):
    print('the result is',a-b)
def multiplication(a,b):
    print('the result is',a*b)
def division(a,b):
    print('the result is',a/b)

if dec=='1':
    addition(a,b)
elif dec =='2':
    subtraction(a,b)
elif dec =='3':
    multiplication(a,b)
elif dec =='4':
    division(a,b)
