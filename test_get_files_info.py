#import os
from functions.get_files_info import get_files_info

print(f'Result for current directory:\n{get_files_info("calculator", ".")}')
#print("\n\n\n\n\n")
print(f'Result for current directory:\n{get_files_info("calculator", "pkg")}')
print(f'Result for current directory:\n{get_files_info("calculator", "/bin")}')
print(f'Result for current directory:\n{get_files_info("calculator", "../")}')
