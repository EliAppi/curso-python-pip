def fibonacci(n):
    '''fibonacci(2)=fibonacci(1)+fibonacci(0) ==> 1+1=2
    fibonacci(3)=fibonacci(2)+fibonacci(1) ==> 2+1=3
    fibonacci(4)=fibonacci(3)+fibonacci(2) ==> 3+2=5
    fibonacci(5)=fibonacci(4)+fibonacci(3) ==> 5+3=8
    '''
    print(n)
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

n=int(input("Escribe un entero: "))
print(fibonacci(n))