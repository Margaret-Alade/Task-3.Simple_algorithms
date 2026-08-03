import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measure_time(sort_func, size):
    arr = [random.randint(0, 1000) for _ in range(size)]
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return end - start

sizes = [100, 500, 1000, 2000, 3000, 5000] 

print("Замеряем время для пузырька, выбором и вставками...")
times_bubble = [measure_time(bubble_sort, size) for size in sizes]
times_selection = [measure_time(selection_sort, size) for size in sizes]
times_insertion = [measure_time(insertion_sort, size) for size in sizes]

print("\nРазмер | Пузырёк (сек) | Выбор (сек) | Вставки (сек)")
print("-------------------------------------------------------")
for i, s in enumerate(sizes):
    print(f"{s:>6} | {times_bubble[i]:.6f} | {times_selection[i]:.6f} | {times_insertion[i]:.6f}")

print("\nВывод графика сравнения трёх сортировок на экран...")
plt.figure(figsize=(10, 6))
plt.plot(sizes, times_bubble, marker='o', linestyle='-', color='red', label='Пузырьковая')
plt.plot(sizes, times_selection, marker='s', linestyle='-', color='blue', label='Выбором')
plt.plot(sizes, times_insertion, marker='^', linestyle='-', color='green', label='Вставками')
plt.title('Сравнение времени выполнения сортировок')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (сек)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("\n--------------------------------------")
print("Выводы:")
print("• Все три сортировки имеют квадратичную сложность O(n²).")
print("• Сортировка вставками часто оказывается быстрее пузырька и выбором, особенно на почти отсортированных данных, но в худшем случае (случайный массив) она также O(n²).")
print("• Сортировка выбором выполняет меньше обменов, чем пузырёк, поэтому обычно быстрее пузырька.")
print("• При больших n (например, >5000) все три становятся слишком медленными для практического использования.")

