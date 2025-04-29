import openpyxl

# Read the Excel file and store the variables in a list of dictionaries
variables_list = []
workbook = openpyxl.load_workbook('variablefile.xlsx')
sheet = workbook.active

# Get the headers from the first row
headers = [cell.value for cell in sheet[1]]

# Skip the first row (header) and start from the second row
for row in sheet.iter_rows(min_row=2, values_only=True):
    if len(row) < len(headers):
        continue  # Skip rows that don't have enough columns
    variables = {headers[i]: str(row[i]) if row[i] is not None else '' for i in range(len(headers))}
    variables_list.append(variables)

# Print the variables list to debug
print("Variables list:")
for variables in variables_list:
    print(variables)

# Read the setcommands file
with open('setcommands.txt', 'r') as file:
    commands_template = file.read()

# Print the original commands to debug
print("Original commands:")
print(commands_template)

# Open the output file in write mode to avoid appending
with open('file1', 'w') as file:
    # Generate and print commands for each row in the Excel file
    for variables in variables_list:
        commands = commands_template
        for key, value in variables.items():
            placeholder = f'{{{key}}}'
            commands = commands.replace(placeholder, value)
        print(f"Commands for {variables.get(headers[0], 'Unknown')}:")
        print(commands)
        print("-" * 40)  # Separator for readability
        # Write the updated commands to the file
        file.write(commands + "\n")

print("The file 'file1' has been generated successfully.")
