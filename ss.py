import os
from typing import List

def generate_folder_structure(path: str, exclusions: List[str], output_file: str) -> None:
    # Nested function to write the folder structure to the output file
    
    def write_tree(current_path: str, prefix: str = '', is_last: bool = False) -> None:
        # Check if the current directory is in the exclusions list
        
        if os.path.basename(current_path) in exclusions:
            return  # Skip this directory if it is excluded

        try:
            # List all items in the current directory
            items = sorted(os.listdir(current_path))
        except FileNotFoundError:
            
            # Handle the case where the directory does not exist
            print(f"Error: The path '{current_path}' does not exist.")
            return

        # Separate items into files and directories
        files = [item for item in items if os.path.isfile(os.path.join(current_path, item))]
        dirs = [item for item in items if os.path.isdir(os.path.join(current_path, item)) and item not in exclusions]

        # Get the name of the current directory
        name = os.path.basename(current_path)
        
        # Write the current directory name to the output file with appropriate prefix
        f.write(f"{prefix}{'└── ' if is_last else '├── '}{name}\n")

        # Create a new prefix for the next level of indentation
        new_prefix = prefix + ('    ' if is_last else '│   ')

        # Write all files in the current directory
        for i, file in enumerate(files):
            
            # Determine if the current file is the last one
            is_last_item = (i == len(files) - 1 and len(dirs) == 0)
            f.write(f"{new_prefix}{'└── ' if is_last_item else '├── '}{file}\n")

        # Recursively write the structure for each directory
        for i, directory in enumerate(dirs):
            
            # Determine if the current directory is the last one
            is_last_dir = (i == len(dirs) - 1)
            write_tree(os.path.join(current_path, directory), new_prefix, is_last_dir)

    # Open the output file for writing the folder structure
    with open(output_file, 'w', encoding='utf-8') as f:
        write_tree(path)  # Start writing the tree from the specified path

if __name__ == "__main__":
    # Define the base path to analyze
    base_path = r'E:/path/of/the/desired/directory'  
    
    # Define the list of folders/files to exclude from the structure
    exclusions = ['venv', '__pycache__', 'migrations', '.git' , 'etc'] 
    
    # Define the output file name
    output_file = 'folder_structure.txt'
    
    # Generate the folder structure
    generate_folder_structure(base_path, exclusions, output_file)
