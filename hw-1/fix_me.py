"""

Скрипт для расчета среднего значения чисел в списке.
"""


def calculate_average(nums):
    """
    Рассчитывает среднее значение чисел в списке.

    Args:
        nums (list): Список чисел.

    Returns:
        float: Среднее значение чисел.
    """
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


def main():
    """
    Основная функция, которая выполняет расчет среднего значения списка
    и выводит результат.
    """
    nums = [10, 15, 20]
    result = calculate_average(nums)
    print("The average is:", result)


if __name__ == "__main__":
    main()
