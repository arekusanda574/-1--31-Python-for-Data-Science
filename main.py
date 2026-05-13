import numpy as np

arr = np.random.randint(1, 101, size=(3, 3))
print("Початковий масив:\n", arr)

total_sum = np.sum(arr)
print("\nСума всіх елементів:", total_sum)

max_val = np.max(arr)
min_val = np.min(arr)
max_idx = np.unravel_index(np.argmax(arr), arr.shape)
min_idx = np.unravel_index(np.argmin(arr), arr.shape)

print(f"\nМаксимальне значення: {max_val}, індекс: {max_idx}")
print(f"Мінімальне значення: {min_val}, індекс: {min_idx}")

sorted_arr = np.sort(arr, axis=1)
print("\nВідсортований масив (по рядках):\n", sorted_arr)