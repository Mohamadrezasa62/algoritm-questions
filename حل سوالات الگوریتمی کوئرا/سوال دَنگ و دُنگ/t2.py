t = int(input())
result = []
for _ in range(t):
    n, s, a = list(map(int, input().split()))
    cost = (s + (n - 1) * a) / n
    cost_per_person = float(cost - a)
    if cost_per_person <= 0 or s == a:
        result.append(-1)
    elif cost_per_person.is_integer():
        result.append(int(cost_per_person))
    else:
        result.append(-1)

for i in result:
    print(i)