#!/usr/bin/python3

for i in range(97, 123):
    if chr(i) not in ['q', 'e']:
        print(chr(i), end='')

# Print a newline at the end using string formatting
print(f'')
