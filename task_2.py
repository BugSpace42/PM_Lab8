def find_triple(n):
    # Находит одну тройку (x, y, z) натуральных чисел таких, что x^2 + y^2 + z^2 = n.
    for x in range(1, n):
        for y in range(x, n):
            for z in range(y, n):
                remainder = n - x * x - y * y - z * z
                if remainder == 0:
                    return (x, y, z)
    return None

n = int(input("Введите n: "))
print(find_triple(n))