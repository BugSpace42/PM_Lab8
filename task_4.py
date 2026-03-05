def task_a():
    result = 0.0
    for i in range(1, 100):
        for j in range(1, 50):
            result += 1 / (i + j**2)
    return result

print(task_a())