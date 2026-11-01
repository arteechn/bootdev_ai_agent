import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
	abs_working_dir = os.path.abspath(working_directory)
	abs_file_path = os.path.abspath(os.path.normpath(os.path.join(working_directory, file_path)))

	valid_target_path = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir

	try:
		if valid_target_path == False:
			return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

		elif os.path.isdir(abs_file_path) == True:
			return f'Error: Cannot write to "{file_path}" as it is a directory'

		else:
			if os.path.isdir(os.path.abspath(os.path.dirname(abs_file_path))) == False:
				os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
			with open(abs_file_path, "w") as f:
				f.write(content)
			return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

	except Exception as e:
		return f'Error: {e}'

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes to file, creating the expected path and file if non existing",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path, relative to working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write into the file",
                },
            },
    	"required": ["file_path", "content"]
        },
    },
}