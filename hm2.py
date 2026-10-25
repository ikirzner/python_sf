# Homework 2

# Exercise 1
# CSV Input: 
col1 = "  Customer ID "
col2 = " Order-Date"
col3 = "TOTAL amount  "
col1 = col1.strip().replace("-","_").replace(" ","_").upper()
col2 = col2.strip().replace("-","_").replace(" ","_").upper()
col3 = col3.strip().replace("-","_").replace(" ","_").upper()
print(f"Column names: \n{col1}, \n{col2}, \n{col3}")
columns = [col1, col2, col3]
print(", ".join(columns))

# Exercise 2
full_name = "raw.sales.orders"
full_name_split = full_name.split(".")
print(full_name_split)
db_name = full_name_split[0].upper()
schema_name = full_name_split[1].upper()
table_name = full_name_split[2].upper()
print(f"Database: {db_name}, Schema: {schema_name}, Table: {table_name}")

# Exercise 3
file_name = "orders_2026-10-25.csv"
# a)
print(file_name.split("_")[0])
# b)
print(file_name.split("_")[1].split(".")[0])
# c)
print(file_name.split(".")[1])
# d) 
print(True if file_name.split(".")[1] == "csv" else False)

# Exercise 4
database = "RAW"
schema = "SALES"
table = "ORDERS"
stage = "ORDERS_STAGE"
skip_header = 1
query = f"""
COPY INTO {database}.{schema}.{table}
FROM @{database}.{schema}.{stage}
FILE_FORMAT = (TYPE = CSV, SKIP_HEADER = {skip_header})
ON_ERROR = 'ABORT_STATEMENT';"""
print(query)


# Exercise 5
rows = 1234567
seconds = 83.456
rejected = 152
print(f"Loaded {rows:,} rows in {seconds:.1f} s (rejected: {rejected/rows:.3%})")

# Exercise 6
s = "Snowflake"
# now
# flake
# ekalfwonS
# -1
# True
# False
# 2
# ['a', 'b', '', 'c']

print(s[1:4])
print(s[-5:])
print(s[::-1])
print(s.find("x"))
print("flake" in s)
print("FLAKE" in s)
print(len("  hi  ".strip()))
print("a,b,,c".split(","))

# Exercise 7
# This is an example of an SQL injection. 
# The problem is that 'date_from_file' can contain any symbol, including '1'='1', that will lead to deletion of all the orders.
# The correct approach is to use parameterized queries. 
# cursor.execute("DELETE FROM staging.orders WHERE order_date = %s", (date_from_file,))