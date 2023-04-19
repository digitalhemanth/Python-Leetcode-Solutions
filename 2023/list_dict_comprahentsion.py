# lists = [4,2,8]

# duble = [num*2 for num in lists]
# print(duble)


# names = ['hemanth','Hem']
# ages = [27,28]

# candiates = {name:age for name in names for age in ages}
# print(candiates)



# records = [    {'id': 1, 'name': 'Alice', 'age': 25},    {'id': 2, 'name': 'Bob', 'age': 35},    {'id': 3, 'name': 'Charlie', 'age': 20},    {'id': 4, 'name': 'David', 'age': 30},    {'id': 5, 'name': 'Eva', 'age': 40},    {'id': 6, 'name': 'Frank', 'age': 22},    {'id': 7, 'name': 'Gina', 'age': 28},    {'id': 8, 'name': 'Henry', 'age': 33},    {'id': 9, 'name': 'Iris', 'age': 27},    {'id': 10, 'name': 'John', 'age': 45}]

# filtered_records = [r for r in records if 25 <= r['age'] <= 30]

# print(filtered_records)


# count = 0
# for r in records:
#     if 25 <= r['age'] <= 30:
#         count += 1

# print(f"Total number of records between 25 and 30 years old: {count}")


# count = len([r for r in records if 25 <= r['age'] <= 30])

# print(f"Total number of records between 25 and 30 years old: {count}")



# Define a list of dictionaries, where each dictionary represents a record
records = [
    {'name': 'John', 'age': 25, 'location': 'New York', 'salary': 50000},
    {'name': 'Emily', 'age': 30, 'location': 'San Francisco', 'salary': 70000},
    {'name': 'Michael', 'age': 40, 'location': 'Los Angeles', 'salary': 90000},
    {'name': 'Sarah', 'age': 28, 'location': 'Chicago', 'salary': 60000},
    {'name': 'David', 'age': 35, 'location': 'Seattle', 'salary': 80000}
]

# Filter the records based on the age range of 25 to 35
filtered_records = [record for record in records if 25 <= record['age'] <= 35]

# # # Create a new dictionary with the filtered records
# filtered_dict = {'filtered_records': filtered_records}

# # # Print the new dictionary
# print(filtered_dict)


# Create a new dictionary with the filtered records
# filtered_dict = {'filtered_records': filtered_records}

# Print the new dictionary
print(filtered_records)
