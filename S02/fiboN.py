def fibon(n):
    i = 0
    sequence = [0, 1]
    while i < (n - 1):
        fibo_v = sequence[-1] + sequence[-2]
        sequence.append(fibo_v)
        i += 1

    print(str(n) + "th Fibonacci term is:" + str(sequence[-1]))

fibon(5)










