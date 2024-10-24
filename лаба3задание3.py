def zadanie_3():
    n = int(input("Введите количество чисел: "))
    numbers = []

    for _ in range(n):
        num = float(input("Введите число: "))
        numbers.append(num)

    sum_odds = 0
    for num in numbers:
        sum_odds += num * (num % 2)
        if num % 2 == 0:
            break

    print("Сумма нечетных чисел в начале последовательности:", sum_odds)


zadanie_3()
