def zadanie_2():
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))

    area = (base * height) / 2
    print("Площадь треугольника:", area)

    if area % 2 == 0:
        area /= 2
        print("Площадь после деления на 2:", area)
    else:
        print("Не могу делить на 2!")


zadanie_2()
