def zadanie_4():
    N = int(input("Введите целое число N (> 0): "))

    count = 0
    total_sum = 0

    while N > 0:
        digit = N % 10
        total_sum += digit
        count += 1
        N //= 10

    print("Количество цифр:", count)
    print("Сумма цифр:", total_sum)


zadanie_4()
