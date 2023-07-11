import argparse
import json

# Create the parser
parser = argparse.ArgumentParser(description="Combine two JSON files")

# Add the arguments
parser.add_argument('json1', type=str, help="The first JSON file")
parser.add_argument('json2', type=str, help="The second JSON file")

# Parse the arguments
args = parser.parse_args()

# Load the first JSON file
with open(args.json1) as f:
    data1 = json.load(f)

# Load the second JSON file
with open(args.json2) as f:
    data2 = json.load(f)

# Combine the two data objects
combined = data1 + data2  # This works if the JSONs are lists
# or
# combined = {**data1, **data2}  # This works if the JSONs are dictionaries

# Write the combined data back into a JSON file
with open('combined.json', 'w') as f:
    json.dump(combined, f, indent=4)

