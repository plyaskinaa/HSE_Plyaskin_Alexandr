def fib(n):

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    try:
        n = int(input("Введите номер числа в последовательности Фибоначчи, на котором следует остановиться: "))
        if n <= 0:
            print("Пожалуйста, введите положительное целое число.")
        else:
            print(f"Последовательность Фибоначчи до {n}-го числа:")
            for index, fibonacci_number in enumerate(fib(n), 1):
                print(f"Fibonacci number {index}: {fibonacci_number}")
    except ValueError:
        print("Пожалуйста, введите целое число.")