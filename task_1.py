def caching_fibonacci():
    cache = {}  # Створити порожній словник cache

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Якщо результат вже є в кеші повертаємо його
        if n in cache:
            return cache[n]

        # Обчислення числа Фібоначчі за допомогою рекурсії
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(10)) 
print(fib(15))
