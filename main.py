def geometric_progression(a, r):
    while True:
        yield a
        a *= r


a = 2
r = 3
gen = geometric_progression(a, r)

for _ in range(5):
    print(next(gen))