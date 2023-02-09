# Store the category titles in a list
categories = ["Prompt", "Removed From Image", "Seed", "Guidance Scale", "Sampler", "Model", "Created", "Additional Credit", "Filter Style"]

# Read the original file line by line
with open('example.txt', 'r') as f:
    lines = f.readlines()

# Remove leading and trailing spaces from each line
lines = [line.strip() for line in lines]

# Initialize the output file
output = []

# Iterate through each line in the file
for i, line in enumerate(lines):
    # Add the first line from the original file to the output
    if i == 0:
        output.append(line)
        output.append('')
        continue
    
    # Check if the line is a category title
    if line in ['Prompt', 'Removed From Image']:
        output.append(line)
        output.append('')
    elif line in ['Seed', 'Guidance Scale', 'Sampler', 'Model', 'Created', 'Additional Credit', 'Filter Style']:
        output.append(line + ':')
    # If it's not a category title, add it to the current line in the output
    else:
        if output[-1] != '':
            output[-1] += ' ' + line
        else:
            output.pop()
            output.append(line)

# Add two empty lines before Prompt, Removed From Image and Seed
if 'Prompt' in output:
    output.insert(output.index('Prompt'), '')
    output.insert(output.index('Prompt'), '')

if 'Removed From Image' in output:
    output.insert(output.index('Removed From Image'), '')
    output.insert(output.index('Removed From Image'), '')

# if line.startswith('Seed'):
#    output.insert(output.index('Seed'), '')
#    output.insert(output.index('Seed'), '')

for i, line in enumerate(output):
    if line.startswith("Seed"):
        output.insert(i, '')
        output.insert(i, '')
        break

# Check for double spaces and replace with single ones
output = [line.replace("  ", " ") for line in output]

# Write the output to a new file
with open('formatted_example.txt', 'w') as f:
    for line in output:
        f.write(line + '\n')
