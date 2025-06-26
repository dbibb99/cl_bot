import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    directory_path = os.path.dirname(abs_file_path)
    if directory_path:
        try: 
            os.makedirs(directory_path, exist_ok=True)
        except Exception as e:
            return f"Error in creating directories: {e}"
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error in writing to {file_path}: {e}"
