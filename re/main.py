import re

# Input string
input_str = "This$#is% Matrix# %!"

# Define the pattern to match special characters
pattern = r'[^\w\s]'

# Replace special characters with spaces
output_str = re.sub(pattern, ' ', input_str)

print(output_str)
