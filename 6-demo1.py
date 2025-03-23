def fun1():
    print("123")
    return 100

fun2 = lambda x:x+100

def fun3(n1 =222 ,n2=333)->int:
    return n1 * n2

fun1()    


print(fun2(100))

print(fun3(n2=1010,n1=200))   

print(fun3())


