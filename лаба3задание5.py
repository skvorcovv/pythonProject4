def zadanie_5():
    numbers = list(map(float, input("Введите числа через пробел: ").split()))

    total_sum = sum(numbers)
    total_product = 1
    for num in numbers:
        total_product *= num

    print("Сумма элементов списка:", total_sum)
    print("Произведение элементов списка:", total_product)


zadanie_5()
