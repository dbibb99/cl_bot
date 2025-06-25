from functions.get_files_info import get_files_info

# calculator / .
print(get_files_info(working_directory='calculator', directory='.'))

# calculator / pkg
print(get_files_info(working_directory='calculator', directory='pkg'))

# calculator / /bin
print(get_files_info(working_directory='calculator', directory='/bin'))

# calculator / ../
print(get_files_info(working_directory='calculator', directory='../'))

# calculator / calculator
print(get_files_info(working_directory='calculator', directory='calculator'))


