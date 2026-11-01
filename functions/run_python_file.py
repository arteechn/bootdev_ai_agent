import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
	abs_working_dir = os.path.abspath(working_directory)
	abs_file_path = os.path.abspath(os.path.normpath(os.path.join(working_directory, file_path)))
	file_ext = os.path.splitext(file_path)
	
	valid_target_path = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir

	try:
		if valid_target_path == False:
			return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'
		
		elif os.path.isfile(abs_file_path) == False:
			return f'Error: "{file_path}" does not exist or is not a regular file'
		
		elif file_ext[1] != ".py":
			return f'Error: "{file_path}" is not a Python file'
		
		else:
			result = ""
			command = ["python", abs_file_path]
			if args is not None:
				command.extend(args)
			success_run = subprocess.run(command, cwd=abs_working_dir, capture_output=True, text=True, timeout=30)

			if success_run.returncode != 0:
				result = f"Process exited with code {success_run.returncode}."
			if success_run.stdout == "" and success_run.stderr == "":
				result += "\nNo output produced."
			else:
				result += f"\nSTDOUT: {success_run.stdout}\nSTDERR: {success_run.stderr}"
			
			return result





	except Exception as e:
		return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes python script from desired file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path, relative to working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                    	"type": "string"
                    },
                    "description": "Arguments given for the script to run on",
                },
            },
    	"required": ["file_path"]
        },
    },
}