def pertence_fibonacci(numero):
    a, b = 0, 1
    while b <= numero:
        if b == numero:
            return f"O número {numero} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {numero} não pertence à sequência de Fibonacci."

numero = 91
print(pertence_fibonacci(numero))