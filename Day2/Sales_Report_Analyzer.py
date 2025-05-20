import numpy as np

sales = np.array([
    50, 55, 53, 60, 62, 58, 54,  # Product 1
    70, 72, 75, 78, 77, 73, 74,  # Product 2
    40, 45, 43, 42, 41, 39, 44,  # Product 3
    90, 88, 85, 87, 89, 86, 84   # Product 4
])

sales_reshaped = sales.reshape(4, 7)

total_sales = np.sum(sales_reshaped, axis=1)
print("Total sales per product:", total_sales)

day5_sales = sales_reshaped[:, 4]
print("Sales on Day 5:", day5_sales)

product2_best_day = np.argmax(sales_reshaped[1])
print("Best day for Product 2 (0-indexed):", product2_best_day)