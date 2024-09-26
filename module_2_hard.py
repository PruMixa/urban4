def get_password(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result


n = 20
password = get_password(n)
print(f"Для числа {n} пароль: {password}")
