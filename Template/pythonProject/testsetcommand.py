import csv

# Read the CSV file and store the variables in a dictionary
variables = {}
with open('variablefile.csv', mode='r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) < 2:
            continue  # Skip rows that don't have at least 2 columns
        variables[row[0]] = row[1]

# Print the variables dictionary to debug
print("Variables dictionary:r")
print(variables)

# Read the setcommands file and replace variables
with open('setcommands.txt', 'r') as file:
    commands = file.read()

# Print the original commands to debug
print("Original commands:")
print(commands)

for key, value in variables.items():
    commands = commands.replace(f'{{{key}}}', value)

# Print the updated commands to debug
print("Updated commands:")
print(commands)

# Write the updated commands to a new file called file1
with open('file1', 'w') as file:
    file.write(commands)

print("The file 'file1' has been generated successfully.")