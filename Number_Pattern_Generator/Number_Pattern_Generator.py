def number_pattern(n):
    a = []

    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n <= 0:
        return "Argument must be an integer greater than 0."

    for _ in range(1, n + 1):
        a.append(_)

    return " ".join(map(str, a))


print(number_pattern(4))
print(number_pattern(12))
