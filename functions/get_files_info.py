import os

# print(os.path.abspath("new_path"))
home = "/home/kaweeka/workspace/github.com/dbibb99/cl_bot/calculator"

def get_files_info(working_directory, directory=None):
    target_directory = os.path.abspath(directory)
    if target_directory != working_directory:
        return f'Error: Cannot list "{target_directory}" as it is outside the permitted working directory'
 
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    else:
        response = []
        dir_contents = os.listdir(directory)
        for content in dir_contents:
            path = os.path.abspath(directory + '/' + content)
            is_dir = os.path.isdir(path)
            size = os.path.getsize(path)
            info = f"- {content}: file_size={size}, is_dir={is_dir}"
            response.append(info)
        return f"this is some of the content: {response}"

print(get_files_info(home, directory="/home/kaweeka/workspace/github.com/dbibb99/cl_bot/calculator"))
