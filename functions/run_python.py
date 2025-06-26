import os
import subprocess


def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ["python3", abs_file_path], capture_output=True, text=True, timeout=30, check=True
            )
        result_info = []
        if result == None:
            return "No output produced"
        std_out = f"STDOUT: {result.stdout}"
        result_info.append(std_out)
        std_err = f"STDERR: {result.stderr}"
        result_info.append(std_err)
        if result.returncode != 0:
            std_code = f"Process exited with code {result.returncode}"
            result_info.append(std_code)
        return "\n".join(result_info)
    except subprocess.CalledProcessError as e:
        return f"Error: executing Python file: {e}"

