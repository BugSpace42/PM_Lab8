import math

def task_a():
    result = 0.0
    for i in range(1, 101):
        for j in range(1, 51):
            result += 1 / (i + j**2)
    return result

def task_b():
    result = 0.0
    for i in range(1, 101):
        for j in range(1, 61):
            result += math.sin(i**3 + j**4)
    return result

def task_c():
    result = 0.0
    for i in range(1, 101):
        for j in range(1, 101):
            result += (j - i + 1) / (i + j)
    return result

def task_d():
    result = 0.0
    for i in range(1, 101):
        for j in range(1, i+1):
            result += 1 / (2 * j + i)
    return result

print(task_a())
print(task_b())
print(task_c())
print(task_d())