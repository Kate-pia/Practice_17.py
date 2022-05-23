array_list = []
num = 0

while True:
    try:
        # преобразование введёной последовательности чисел в список
        array_list = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
        break
    except ValueError:
        print('Введено неверное значение')

while True:
    try:
        num = int(input("Введите число: "))
        break
    except ValueError:
        print('Введено неверное значение')

array_list.append(num)  # добавляем элемент в список


def sel_sort(array):  # Применяем сортировку выбором
    for i in range(len(array)):  # проходим по всему массиву
        idx_min = i  # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:  # если индекс не совпадает с минимальным, меняем
            array[i], array[idx_min] = array[idx_min], array[i]
    return array


def binary_search(array, element, left, right):  # Алгоритм двоичного поиска
    if left > right:  # если левая граница превысила правую,
        return print("Число не найдено")  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle - 1  # возвращаем индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


sort_array = sel_sort(array_list)  # сортируем список элементов


if num == sort_array[0] or num == sort_array[-1]:
    print("Введенное число не удовлетворяет условию задачи")
else:
    print("Номер позиции элемента =", binary_search(sort_array, num, 0, len(sort_array) - 1))
