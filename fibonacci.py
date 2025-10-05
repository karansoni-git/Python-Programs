def fibonacci(num):
    first = 0
    second = 1
    series = [first,second]
    for i in range(num):
        next = first + second
        first = second
        second = next
        series.append(next)
    print(series)
fibonacci(8)