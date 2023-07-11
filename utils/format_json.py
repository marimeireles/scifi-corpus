import json

def format_json(input_file, output_file, indent=4):
    # Open the input JSON file for reading
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Open the output file for writing
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=indent)

input_file = 'everythingminusgutenberg.json'  # specify your input json file here
output_file = 'clean_everythingminusgutenberg.json'  # specify your output file here

format_json(input_file, output_file)

