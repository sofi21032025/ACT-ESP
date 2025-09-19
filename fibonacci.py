def fibonacci(n):
    serie = [0, 1]  
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie


fibo = fibonacci(10000)

for i, num in enumerate(fibo, start=1):
    print(f"{i}: {num}")

