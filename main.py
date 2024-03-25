from datetime import datetime, timedelta

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
def range_generator(start, stop):
    current = start
    while current < stop:
        yield current
        current += 1


for i in range_generator(0, 10):
    print(i)


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
def square_generator(a, n):
    while a < n:
        yield a ** 3
        a += 1


cube_list = list(square_generator(2, 10))
print(cube_list)


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
def date_range_generator(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)


start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 10)

for date in date_range_generator(start_date, end_date):
    print(date.strftime('%Y-%m-%d'))