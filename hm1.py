# Exercise 1
db = "RAW"
schema = "SALES"
table = "ORDERS"
row_count = 250000
is_loaded = True
print(f"Table {db}.{schema}.{table} has {row_count} rows. Loaded: {is_loaded}")

# Exercise 2
qty = "7"
unit_price = "12.50"
total_price = float(qty) * float(unit_price)
print(f"Total price = {total_price}")

print(type(total_price)) 

# Exercise 3
total_rows = 1_234_567
batch_size = 50_000
full_batches = total_rows // batch_size
print(f"Full batches: {full_batches}")
rows_last_batch = total_rows % batch_size
print(f"Rows in last batch: {rows_last_batch}")
batch_count = full_batches + (1 if rows_last_batch > 0 else 0)
print(f"Total number of batches: {batch_count}")

# Exercise 4
print(type(3 / 1))
print("5" * 3)
print(int("  42  "))
print(int(7.9))
print(bool(0), bool(""), bool("False"))

# Exercise 5
# If the customer's email is NULL, then in Python this value will be None. 
# In a data pipeline, an empty string may be a valid value (e.g. for the customer's email), but a None will not be a valid value. 
# Therefore, None values need to be handled separately in the code.