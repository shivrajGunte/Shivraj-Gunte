
a = int(input("Enter a: "))
result = []

for i in range(a):
    result.append(2 * i + 1)

print(", ".join(map(str, result)))
