import sqlite3

# Define a function to write to a log file
def write_to_log(message):
    with open("database_operations.log", "a") as log_file:
        log_file.write(message + "\n")

# Connect to the SQLite database
conn = sqlite3.connect('AAPL.db')
cursor = conn.cursor()

# CRUD Operations

# 1. Create: Add a new record.
create_data = ('2023-10-01', '150.00', '155.00', \
            '149.00', '154.50', '154.40', '5000000')
cursor.execute('INSERT INTO my_table (Date, Open, High, \
            Low, Close, Adj, Volume) VALUES (?, ?, ?, ?, ?, ?, ?)', create_data)
conn.commit()
write_to_log("Record with date '2023-10-01' created successfully.")

# 2. Read: Fetch and display the first 5 records.
cursor.execute("SELECT * FROM my_table LIMIT 5")
read_data = cursor.fetchall()
print(read_data)
write_to_log("First 5 records fetched successfully.")

# 3. Update: Modify the 'Open' value of the record with the date '2023-10-01'.
cursor.execute("UPDATE my_table SET Open = '151.00' WHERE Date = '2023-10-01'")
conn.commit()
write_to_log("Record with date '2023-10-01' updated successfully.")

# 4. Delete: Remove the record with the date '2023-10-01'.
cursor.execute("DELETE FROM my_table WHERE Date = '2023-10-01'")
conn.commit()
write_to_log("Record with date '2023-10-01' deleted successfully.")


# Additional SQL Queries

# 1. Query to fetch the total number of records.
cursor.execute("SELECT COUNT(*) FROM my_table")
total_records = cursor.fetchone()
write_to_log(f"Total number of records: {total_records[0]}")

# 2. Query to fetch records where the `High` value is above '160.00'.
cursor.execute("SELECT * FROM my_table WHERE High > '160.00' LIMIT 5")
high_value_records = cursor.fetchall()
write_to_log(f"Number of records with High value above 160.00: \
            {len(high_value_records)}")

conn.close()
