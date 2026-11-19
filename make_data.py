import csv
import random
from datetime import date, timedelta

random.seed(42)

categories = {
    "Electronics": ["Laptop", "Phone", "Headphones", "Monitor"],
    "Office": ["Desk Chair", "Notebook", "Pen Set", "Printer"],
    "Home": ["Lamp", "Coffee Maker", "Blender", "Rug"],
    "Sports": ["Yoga Mat", "Dumbbell", "Bicycle", "Tennis Racket"],
}

customers = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hovhannes"]

prices = {
    "Laptop": 900, "Phone": 650, "Headphones": 120, "Monitor": 300,
    "Desk Chair": 180, "Notebook": 8, "Pen Set": 15, "Printer": 220,
    "Lamp": 45, "Coffee Maker": 95, "Blender": 70, "Rug": 150,
    "Yoga Mat": 35, "Dumbbell": 60, "Bicycle": 400, "Tennis Racket": 110,
}

start = date(2024, 1, 1)
rows = []

for order_id in range(1, 51):
    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])
    quantity = random.randint(1, 4)
    order_date = start + timedelta(days=random.randint(0, 364))
    rows.append({
        "order_id": order_id,
        "order_date": order_date.isoformat(),
        "customer": random.choice(customers),
        "category": category,
        "product": product,
        "quantity": quantity,
        "price": prices[product],
    })

with open("sales.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["order_id", "order_date", "customer",
                                           "category", "product", "quantity", "price"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Created sales.csv with {len(rows)} rows")
