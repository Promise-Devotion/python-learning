from pathlib import Path

cwd = Path.cwd()
print('\nCurrent working directory:\n' + str(cwd))

# Create full path name by joining path and filename
new_file = Path.joinpath(cwd, 'new_file.txt')
print('\nFull path:\n' + str(new_file))

# Check if file exists
print('\nDoes that file exist? ' + str(new_file.exists()) + '\n')