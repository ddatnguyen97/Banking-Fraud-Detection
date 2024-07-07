import pandas as pd
import os

def split_csv(file_path, batch_size):
    with open(file_path, 'r') as file:
        header = file.readline()
        csv_lines = file.readlines()
    
    filename = 1
    base_name, ext = os.path.splitext(os.path.basename(file_path))

    for i in range(0, len(csv_lines), batch_size):
        with open(f'{base_name}_part{filename}{ext}', 'w') as batch_file:
            batch_file.write(header)
            batch_file.writelines(csv_lines[i:i + batch_size])
        filename += 1

# split_csv('fraudTrain.csv', 300000)
# split_csv('fraudTest.csv', 300000)
    