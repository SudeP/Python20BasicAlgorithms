# 0 ile 1000 arasındaki Fibonacci sayılarını bulan programı yazınız?
# Öğrendiklerim
# yok

prev = 0
fibonacciNumbers = []

def fibonacci(curr):
    global fibonacciNumbers, prev

    next = prev + curr

    if(next > 1000):
        return
    
    fibonacciNumbers.append(next)

    prev = curr

    fibonacci(next)


fibonacci(1)

print('0 ile 1000 arasındaki Fibonacci sayıları', fibonacciNumbers)