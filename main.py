import numpy as np

# Завдання 1: Одновимірний масив з першими 10-ма натуральними числами
vector1 = np.arange(1, 11)
print("Одновимірний масив з першими 10-ма натуральними числами:")
print(vector1)

# Завдання 2: Двовимірний масив розміром 3x3 з нулями
matrix2 = np.zeros((3, 3))
print("\nДвовимірний масив розміром 3x3 з нулями:")
print(matrix2)

# Завдання 3: Масив розміром 5x5 з випадковими цілими числами в діапазоні від 1 до 10
matrix3 = np.random.randint(1, 11, (5, 5))
print("\nМасив розміром 5x5 з випадковими цілими числами в діапазоні від 1 до 10:")
print(matrix3)

# Завдання 4: Масив розміром 4x4 з випадковими дійсними числами в діапазоні від 0 до 1
matrix4 = np.random.rand(4, 4)
print("\nМасив розміром 4x4 з випадковими дійсними числами в діапазоні від 0 до 1:")
print(matrix4)

# Завдання 5: Два одновимірних масиви розміром 5 з випадковими цілими числами в діапазоні від 1 до 10
vector5_1 = np.random.randint(1, 11, 5)
vector5_2 = np.random.randint(1, 11, 5)

# Поелементні операції додавання, віднімання та множення
sum_result = vector5_1 + vector5_2
subtraction_result = vector5_1 - vector5_2
multiplication_result = vector5_1 * vector5_2

print("\nДва одновимірних масиви розміром 5 з випадковими цілими числами:")
print("Перший масив:", vector5_1)
print("Другий масив:", vector5_2)
print("Результат додавання:", sum_result)
print("Результат віднімання:", subtraction_result)
print("Результат множення:", multiplication_result)

# Завдання 6: Два вектори розміром 7 з довільними числами та знаходження скалярного добутку
vector6_1 = np.random.randint(1, 11, 7)
vector6_2 = np.random.randint(1, 11, 7)
dot_product = np.dot(vector6_1, vector6_2)

print("\nДва вектори розміром 7 з довільними числами:")
print("Перший вектор:", vector6_1)
print("Другий вектор:", vector6_2)
print("Скалярний добуток:", dot_product)

# Завдання 7: Дві матриці розміром 2x2 та 2x3 з випадковими цілими числами в діапазоні від 1 до 10 та їх перемноження
matrix7_1 = np.random.randint(1, 11, (2, 2))
matrix7_2 = np.random.randint(1, 11, (2, 3))
product_matrix7 = np.dot(matrix7_1, matrix7_2)

print("\nДві матриці розміром 2x2 та 2x3 з випадковими цілими числами:")
print("Перша матриця:")
print(matrix7_1)
print("Друга матриця:")
print(matrix7_2)
print("Результат перемноження:")
print(product_matrix7)

# Завдання 8: Матриця розміром 3x3 з випадковими цілими числами в діапазоні від 1 до 10 та знаходження оберненої матриці
matrix8 = np.random.randint(1, 11, (3, 3))
inverse_matrix8 = np.linalg.inv(matrix8)

print("\nМатриця розміром 3x3 з випадковими цілими числами в діапазоні від 1 до 10:")
print(matrix8)
print("Обернена матриця:")
print(inverse_matrix8)

# Завдання 9: Матриця розміром 4x4 з випадковими дійсними числами в діапазоні від 0 до 1 та транспонування
matrix9 = np.random.rand(4, 4)
transpose_matrix9 = np.transpose(matrix9)

print("\nМатриця розміром 4x4 з випадковими дійсними числами в діапазоні від 0 до 1:")
print(matrix9)
print("Транспонована матриця:")
print(transpose_matrix9)

# Завдання 10: Матриця розміром 3x4 та вектор розміром 4 з випадковими цілими числами та їх перемноження
matrix10 = np.random.randint(1, 11, (3, 4))
vector10 = np.random.randint(1, 11, 4)
product_matrix10 = np.dot(matrix10, vector10)

print("\nМатриця розміром 3x4 та вектор розміром 4 з випадковими цілими числами:")
print("Матриця:")
print(matrix10)
print("Вектор:")
print(vector10)
print("Результат перемноження:")
print(product_matrix10)

# Завдання 11: Матриця розміром 2x3 та вектор розміром 3 з випадковими дійсними числами та їх перемноження
matrix11 = np.random.rand(2, 3)
vector11 = np.random.rand(3)
product_matrix11 = np.dot(matrix11, vector11)

print("\nМатриця розміром 2x3 та вектор розміром 3 з випадковими дійсними числами:")
print("Матриця:")
print(matrix11)
print("Вектор:")
print(vector11)
print("Результат перемноження:")
print(product_matrix11)

# Завдання 12: Дві матриці розміром 2x2 та їхнє поелементне множення
matrix12_1 = np.random.randint(1, 11, (2, 2))
matrix12_2 = np.random.randint(1, 11, (2, 2))
elementwise_product_matrix12 = matrix12_1 * matrix12_2

print("\nДві матриці розміром 2x2 з випадковими цілими числами:")
print("Перша матриця:")
print(matrix12_1)
print("Друга матриця:")
print(matrix12_2)
print("Результат поелементного множення:")
print(elementwise_product_matrix12)

# Завдання 13: Дві матриці розміром 2x2 та їхній добуток
matrix13_1 = np.random.randint(1, 11, (2, 2))
matrix13_2 = np.random.randint(1, 11, (2, 2))
product_matrix13 = np.dot(matrix13_1, matrix13_2)

print("\nДві матриці розміром 2x2 з випадковими цілими числами:")
print("Перша матриця:")
print(matrix13_1)
print("Друга матриця:")
print(matrix13_2)
print("Результат добутку:")
print(product_matrix13)

# Завдання 14: Матриця розміром 5x5 з випадковими цілими числами в діапазоні від 1 до 100 та знаходження суми елементів
matrix14 = np.random.randint(1, 101, (5, 5))
sum_of_elements_matrix14 = np.sum(matrix14)

print("\nМатриця розміром 5x5 з випадковими цілими числами в діапазоні від 1 до 100:")
print(matrix14)
print("Сума елементів матриці:", sum_of_elements_matrix14)

# Завдання 15: Дві матриці розміром 4x4 з випадковими цілими числами в діапазоні від 1 до 10 та їхня різниця
matrix15_1 = np.random.randint(1, 11, (4, 4))
matrix15_2 = np.random.randint(1, 11, (4, 4))
difference_matrix15 = matrix15_1 - matrix15_2

print("\nДві матриці розміром 4x4 з випадковими цілими числами:")
print("Перша матриця:")
print(matrix15_1)
print("Друга матриця:")
print(matrix15_2)
print("Різниця матриць:")
print(difference_matrix15)

# Завдання 16: Матриця розміром 3x3 з випадковими дійсними числами в діапазоні від 0 до 1 та знаходження вектора-стовпця, що містить суму елементів кожного рядка матриці
matrix16 = np.random.rand(3, 3)
sum_of_rows_matrix16 = np.sum(matrix16, axis=1)
column_vector_sum_of_rows_matrix16 = sum_of_rows_matrix16.reshape(-1, 1)

print("\nМатриця розміром 3x3 з випадковими дійсними числами в діапазоні від 0 до 1:")
print(matrix16)
print("Сума елементів кожного рядка:")
print(column_vector_sum_of_rows_matrix16)

# Завдання 17: Матриця розміром 3x4 з довільними цілими числами та створення матриці з квадратами цих чисел
matrix17 = np.random.randint(-10, 11, (3, 4))
square_matrix17 = np.square(matrix17)

print("\nМатриця розміром 3x4 з довільними цілими числами:")
print(matrix17)
print("Матриця з квадратами чисел:")
print(square_matrix17)

# Завдання 18: Вектор розміром 4 з випадковими цілими числами в діапазоні від 1 до 50 та знаходження вектора з квадратними коренями цих чисел
vector18 = np.random.randint(1, 51, 4)
sqrt_vector18 = np.sqrt(vector18)

print("\nВектор розміром 4 з випадковими цілими числами в діапазоні від 1 до 50:")
print(vector18)
print("Вектор з квадратними коренями:")
print(sqrt_vector18)
