def bubble_sort(arr):
    """Сортировка пузырьком по возрастанию."""
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    print("Программа сортировки пузырьком по возрастанию.")
    n = int(input("Введите количество чисел: "))
    numbers = [int(input(f"Число {i + 1}: ")) for i in range(n)]

    bubble_sort(numbers)
    print("Отсортированные числа:", numbers)


if __name__ == "__main__":
    main()
