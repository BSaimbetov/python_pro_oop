#Task 1
def geometric_progression(a, r):
    while True:
        yield a
        a *= r


a = 2
r = 3
gen = geometric_progression(a, r)

for _ in range(5):
    print(next(gen))

#Task 2
def range_generator(*args):

    start, stop, step = 0, None, 1#
    if not all(isinstance(arg, int) for arg in args):
        raise TypeError("All arguments must be integers")
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError
    if step == 0:
        raise ValueError("Step cannot be zero")
    for i in range(start, stop, step):
        yield i


print(*range_generator(10))
print(*range_generator(1, 10))
print(*range_generator(1, 10, 2.2))
print(*range_generator(10, 1, -2))

#Task 3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator(end):
    for num in range(end + 1):
        if is_prime(num):
            yield num


for prime in prime_generator(20):
    print(prime)

#Task 4
cubes_list = [i ** 3 for i in range(2, 10)]
print(cubes_list)

#Task 5
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))

#Task 6
from datetime import datetime, timedelta
def date_range_generator(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)


start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 10)

for date in date_range_generator(start_date, end_date):
    print(date.strftime('%Y-%m-%d'))
