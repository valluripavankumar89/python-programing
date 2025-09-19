import csv

data = [['hi', 2, 4, 5], [6, 9, 2, 8]]

# Writing to CSV
with open('Table.csv', 'w', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerows(data)

# Reading and printing
with open('Table.csv', 'r') as fp:
    for row in fp:
        print(row.strip())

