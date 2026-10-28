# Exercise 1
files = ["orders_2026-10-23.csv", "customers_2026-10-23.csv", "orders_2026-10-24.csv", "orders_2026-10-25.csv"]

print(len(files))
files.append("customers_2026-10-24.csv")
print(files)
sorted_files = sorted(files)
print(sorted_files)
print(files)
print(files[-2:])
print("orders_2026-10-22.csv" in files)
var = files.pop(0)
print(var)
print(files)

# Exercise 2
rows = [
    (1001, "Alice", 250.0),
    (1002, "Bob", None),
    (1003, "Chen", 99.5),
]

order_id, customer, amount = rows[1]
print(f"Order ID: {order_id}, Customer: {customer}, Amount: {amount}")
print(rows[2][2])
print(rows[0][2] + rows[2][2])
print(sum(row[2] for row in rows if row[2] is not None))

# Exercise 3
config = {
    "account": "xy12345",
    "user" : "etl_user",
    "warehouse" : "COMPUTE_WH",
    "database" : "RAW",
    "schema" : "SALES"
    }

print(config["warehouse"])
config["warehouse"] = "LOAD_WH"
config["role"] = "ETL_ROLE"
print(config)
config_sorted = dict(sorted(config.items()))
print(config_sorted)

# Exercise 4
event = {
    "event_id": "e-981",
    "customer": {
        "id": 1042,
        "name": "Alice",
        "address": {"city": "Berlin", "country": "DE"},
    },
    "items": [
        {"sku": "A-1", "qty": 2, "price": 9.99},
        {"sku": "B-7", "qty": 1, "price": 24.50},
    ],
    "coupon": None,
}

print(event["customer"]["address"]["country"])
print(event["items"][1]["sku"])
print(event["items"][0]["qty"] * event["items"][0]["price"])
print(len(event["items"]))

# Exercise 5