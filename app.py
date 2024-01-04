import os

# Size of each file in bytes (1 MiB = 1024 * 1024 bytes)
file_size = 1024 * 1024

# Content to write to each file
content = 'a' * file_size

# Create 1000 files
for i in range(1000):
    filename = f'file_{i}.txt'
    print(f'Creating {filename}')
    with open(filename, 'w') as f:
        f.write(content)