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

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def measure_time(sort_func, size):
    arr = [random.randint(0, 1000) for _ in range(size)]
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return end - start

sizes = [100, 500, 1000, 2000, 3000, 5000] 

print("Замеряем время для пузырька и выбором...")
times_bubble = [measure_time(bubble_sort, size) for size in sizes]
times_selection = [measure_time(selection_sort, size) for size in sizes]

print("\nРазмер | Пузырёк (сек) | Выбор (сек)")
print("--------------------------------------")
for i, s in enumerate(sizes):
    print(f"{s:>6} | {times_bubble[i]:.6f} | {times_selection[i]:.6f}")

print("\nВывод графика сравнения сортировки пузырьком и выбором на экран...")
plt.figure(figsize=(10, 6))
plt.plot(sizes, times_bubble, marker='o', linestyle='-', color='red', label='Пузырьковая')
plt.plot(sizes, times_selection, marker='s', linestyle='-', color='blue', label='Выбором')
plt.title('Сравнение времени выполнения сортировок')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (сек)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("\n--------------------------------------")
print("Выводы:")
print("• Обе сортировки имеют квадратичную сложность O(n²).")
print("• Сортировка выбором обычно работает быстрее пузырька, т.к. делает меньше обменов.")
print("• Рост времени пропорционален n² – это видно по изгибу графика (не линейный).")
print("• Для больших массивов (n > 5000) время становится неприемлемо большим.")

