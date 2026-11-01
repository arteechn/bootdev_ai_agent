from functions.get_file_content import get_file_content

def main() -> None:
	item_list = ["lorem.txt", "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]

	for item in item_list:
		result = get_file_content("calculator", item)
		print(f"{item} length: {len(result)}")
		print(f"{item} truncated: {'truncated' in result}")
		print(result)


if __name__ == "__main__":
    main()
#result = get_file_content("calculator", "lorem.txt")
#print(f"lorem.txt length: {len(result)}")
#print(f"lorem.txt truncated: {'truncated' in result}")
