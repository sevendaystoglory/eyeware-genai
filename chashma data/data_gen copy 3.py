import pandas as pd

# List of input file paths
input_files = []
for i in range(1,51):
    filename="model"+str(i)+".xlsx"
    input_files.append(filename)

# Output file path
output_file = 'merged_file.xlsx'

# Create a Pandas Excel writer using the output file path
writer = pd.ExcelWriter(output_file)

# Iterate over input files
for file in input_files:
    # Read each input file into a Pandas DataFrame
    df = pd.read_excel(file)
    
    # Extract the file name without extension as the sheet name
    sheet_name = file.split('.')[0]
    
    # Write the DataFrame to the output file as a new sheet
    df.to_excel(writer, sheet_name=sheet_name, index=False)

# Save and close the Excel writer
writer.save()
writer.close()
