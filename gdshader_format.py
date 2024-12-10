import re
import os

def format_shader_file(file_path: str):
    """Format single Godot Shader file"""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        shader_code = file.read()

    # Split code lines and remove excessive whitespace.
    lines = shader_code.splitlines()

    # Define the indentation level and result list.
    indent_level = 0
    formatted_lines = []
    indent_space = "  " 

    for line in lines:
        line = line.strip()
        if not line:
            formatted_lines.append("")
            continue

        # Check for block ending symbols
        if re.match(r"(.*}\s*)", line):
            indent_level = max(indent_level - 1, 0)

        # Add indentation and save
        formatted_lines.append(f"{indent_space * indent_level}{line}")

        # Check for block starting symbols
        if re.match(r".*{\s*$", line):
            indent_level += 1

    # Merge the formatted code
    formatted_code = "\n".join(formatted_lines)

    # Write file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_code)

    print(f"Formatted shader file: {file_path}")

def format_all_shaders_in_folder(folder_path: str):
    """format all .gdshader file under the folder path"""
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".gdshader"):
                file_path = os.path.join(root, file_name)
                format_shader_file(file_path)

if __name__ == "__main__":
    shaders_folder = "shaders/"  # replace to actual folder path
    format_all_shaders_in_folder(shaders_folder)
