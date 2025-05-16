import random
import csv
from datetime import timedelta

csv_path = "restaurant_queue_simulation.csv"

num_clients = 12

min_dish_time = 5
max_dish_time = 20
min_cash_time = 5
max_cash_time = 35
max_dishes = 6

clients_data = []

current_time = 0

for client_id in range(1, num_clients + 1):
    num_dishes = random.randint(1, max_dishes)
    dish_selection_time = sum(random.randint(min_dish_time, max_dish_time) for _ in range(num_dishes))
    queue_entry_time = current_time + dish_selection_time
    waiting_time = max(0, current_time - queue_entry_time)
    cash_time = random.randint(min_cash_time, max_cash_time)
    total_time = dish_selection_time + waiting_time + cash_time

    clients_data.append({
        "client_id": client_id,
        "queue_number": len(clients_data) + 1,
        "entry_time": timedelta(seconds=queue_entry_time),
        "dish_time": timedelta(seconds=dish_selection_time),
        "wait_time": timedelta(seconds=waiting_time),
        "cash_time": timedelta(seconds=cash_time),
        "total_time": timedelta(seconds=total_time)
    })

    current_time = queue_entry_time + waiting_time + cash_time

with open(csv_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "# клієнта", "# у черзі", "Час входу в чергу",
        "Тривалість вибору страв", "Тривалість на касі",
        "Повний час обслуговування"
    ])
    for data in clients_data:
        writer.writerow([
            data["client_id"],
            data["queue_number"],
            str(data["entry_time"]),
            f"{int(data['dish_time'].total_seconds())} секунд",
            f"{int(data['cash_time'].total_seconds())} секунд",
            str(data["total_time"])
        ])

print(f"Program completed (review \'{csv_path}\').")