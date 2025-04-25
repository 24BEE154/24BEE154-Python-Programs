print("Name:Shubh Raval")
print("Roll no.:24BEE154")
import csv

filename = 'excel_data.csv'

header = ['ID', 'Name', 'Department', 'Salary']
data = [
    [1, 'Alice Johnson', 'HR', 50000],
    [2, 'Bob Smith', 'Engineering', 75000],
    [3, 'Charlie Lee', 'Marketing', 62000],
    [4, 'Dana Kim', 'Finance', 67000]
]
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(header)
    
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully. You can open it directly in MS-Excel.")
