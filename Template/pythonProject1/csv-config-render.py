import csv
from jinja2 import Template
from pprint import pprint

# Function to read CSV file and return data as a list of dictionaries
def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

# Function to render template with data and write to output file
def render_template(template_path, data, output_path):
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    template = Template(template_content)
  
    rendered_content = template.render(data=data)
    
    with open(output_path, 'w') as file:
        file.write(rendered_content)

# Example usage
csv_file_path = 'input.csv'
template_file_path = 'template.j2'
output_file_path = 'output.txt'

data = read_csv(csv_file_path)

render_template(template_file_path, data, output_file_path)

print(f"Data from {csv_file_path} has been rendered using {template_file_path} and saved to {output_file_path}.")