def gcd_two_numbers(a, b):
    # Вычисляет НОД двух чисел с помощью алгоритма Евклида.]
    while b != 0:
        a, b = b, a % b
    return a

m = int(input("Введите m: "))
n = []
for i in range(1, m + 1):
    n.append(int(input(f"Введите m_{i}: ")))
print(n)