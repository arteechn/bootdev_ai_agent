import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
    valid_target_path = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
    
    print(abs_working_dir)

    try:
        if valid_target_path is False:
            error_not_valid = f'\tError: Cannot list "{directory}" as it is outside the permitted working directory'
            return error_not_valid

        if os.path.isdir(target_dir) == False:
            error_not_a_path = f'\tError: "{directory}" is not a directory'
            return error_not_a_path

        else:
            files_list = []

            for item in os.listdir(target_dir):                
                full_path = os.path.normpath(os.path.join(target_dir, item))
                size = os.path.getsize(full_path)
                is_dir = os.path.isdir(full_path)
                
                file_info_string = ', '.join([f'file_size={size} bytes', f'is_dir={is_dir}'])
                files_list.append(f"    - {item}: {file_info_string}")

            result = "\n".join(files_list)
            return result
            


    except Exception as e:
        error_exception = f'Error: Some other error I still need to debug and understand \n\n{e}'
        return error_exception
    

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

