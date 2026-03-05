def find_triples(n):
    # Находит все тройки (x, y, z) натуральных чисел таких, что x^2 + y^2 + z^2 = n.
    triples = []
    for x in range(1, n):
        for y in range(x, n):
            for z in range(y, n):
                remainder = n - x * x - y * y - z * z
                if remainder == 0:
                    triples.append((x, y, z))
    return triples

n = int(input("Введите n: "))
triples = find_triples(n)
if triples:
    print(f"Есть {len(triples)} троек натуральных чисел таких, что x^2 + y^2 + z^2 = n:")
    print(*triples, sep="\n")
else:
    print("Таких троек нет.")