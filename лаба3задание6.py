def zadanie_6():
    numbers = list(map(float, input("Введите числа через пробел: ").split()))

    average = sum(numbers) / len(numbers)

    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = average

    print("Измененный массив:", numbers)


zadanie_6()
