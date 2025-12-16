# Input
item_count = int(input("Enter the number of items: "))
bag_capacity = int(input("Enter the bag capacity: "))

weights = []
values = []

for i in range(item_count):
    weights.append(int(input(f"Enter the weight of item {i+1}: ")))
    values.append(int(input(f"Enter the value of item {i+1}: ")))

# Create list of (weight, value, value/weight)
items = []
for i in range(item_count):
    items.append((weights[i], values[i], values[i] / weights[i]))

# Sort items by value per weight in descending order
items.sort(key=lambda x: x[2], reverse=True)

total_weight = 0
total_value = 0

# Fractional Knapsack Logic
for weight, value, ratio in items:
    if total_weight + weight <= bag_capacity:
        total_weight += weight
        total_value += value
    else:
        remaining = bag_capacity - total_weight
        total_value += ratio * remaining
        break

print(f"Maximum value in bag = {total_value}")
