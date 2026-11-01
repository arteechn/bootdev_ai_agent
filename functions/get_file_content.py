import os
from constants import MAX_CHARS



def get_file_content(working_directory: str, file_path: str) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.normpath(os.path.join(working_directory, file_path)))

    valid_target_path = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir

    try:    
        if valid_target_path == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        elif os.path.isfile(abs_file_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        else:
            with open(abs_file_path, "r") as f:
                file_content = f.read(MAX_CHARS)
                if f.read(1):
                    file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return file_content



    except Exception as e:
        return 'Error:\n{e}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Provides content in provided file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path, relative to working directory",
                },
            },
        "required": ["file_path"]
        },
    },
}