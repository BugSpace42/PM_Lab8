def gcd_two_numbers(a, b):
    # Вычисляет НОД двух чисел с помощью алгоритма Евклида.
    while b != 0:
        a, b = b, a % b
    return a


def gcd_multiple_numbers(numbers):
    result = gcd_two_numbers(numbers[0], numbers[1])
    for i in range(2, len(numbers)):
        result = gcd_two_numbers(result, numbers[i])
    return result

m = int(input("Введите m: "))
n = []
for i in range(1, m + 1):
    n.append(int(input(f"Введите m_{i}: ")))
result = gcd_multiple_numbers(n)
print(f"НОД введённых чисел равен {result}")
