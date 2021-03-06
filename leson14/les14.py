# Решить с помощью генераторов списка.

# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.

from math import sqrt
fruits_list1 = ['banana', 'orange', 'apple', 'pineapple', 'kiwi', 'lemon']
fruits_list2 = ['apricot', 'lemon', 'orange']
print([i for i in fruits_list1 if fruits_list2.count(i) == 1])


# 2: Дан список, заполненный произвольными числами. Получить список из элементов исходного,
# удовлетворяющих следующим условиям:
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.
#     Примечание: Список с целыми числами создайте вручную в начале файла.
#     Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.

my_list = [12, -3, 3, 9, 10, -9, 0, 1, 15, 3]
print([i for i in my_list if i >= 3 and i % 3 == 0 and i % 4 != 0])


# 3. Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
# и самих чисел (если число отрицательное) и возвращает результат
# (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
#     Примечание: Список с целыми числами создайте вручную в начале файла.
#     Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.


def create_list(old_list):
    return [int(sqrt(i)) if i > 0 else i for i in old_list]


print(create_list([1, -3, 4]))


# 4. Написать функцию которая принимает на вход число от 1 до 100.
# Если число равно 13, функция поднимает исключительную ситуации ValueError иначе возвращает введенное число,
# возведенное в квадрат.
# Далее написать основной код программы.
# Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция.
# Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.

def Try_Ex(num):
    if num < 1 or num > 100 or num == 13:
        raise ValueError
    else:
        return num**2


try:
    print(f"Your number is squared = {Try_Ex(int(input('Enter number (1-100): ')))}")
except ValueError:
    print('I dont like this number. Good bye!')
