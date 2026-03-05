def is_perfect(num):
    if num < 2:
        return False
    divisors_sum = 1  # 1 является делителем у любого числа
    for i in range(2, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

n = int(input("Введите n: "))
perfects = []
for i in range(2, n):
    if is_perfect(i):
        perfects.append(i)
print(f"Есть {len(perfects)} совершенных чисел, меньших {n}:")
print(*perfects, sep="\n")