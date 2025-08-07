
a = int(input("Enter a: "))
result = []

for i in range(1, a + 1):
    if i % 2 == 1:
        result.append(2 * (i // 2) + 1)

print(", ".join(map(str, result)))
