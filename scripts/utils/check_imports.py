import os
import re
import ast
import importlib

def find_python_files(repo_path):
    python_files = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def extract_imports_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    import_statements = re.findall(r'^(?:from\s+\S+\s+import\s+\S+|import\s+\S+)', content, re.MULTILINE)
    return import_statements

def collect_all_imports(repo_path):
    python_files = find_python_files(repo_path)
    all_imports = {}
    
    for file in python_files:
        imports = extract_imports_from_file(file)
        if imports:
            all_imports[file] = imports
    
    return all_imports

def remove_bom(content):
    BOM = '\ufeff'
    if content.startswith(BOM):
        return content[len(BOM):]
    return content

def get_used_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = remove_bom(file.read())
        tree = ast.parse(content, filename=file_path)
    
    used_names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used_names.add(node.id)
        elif isinstance(node, ast.Attribute):
            used_names.add(node.attr)
    
    return used_names

def find_unused_imports(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = remove_bom(file.read())
        tree = ast.parse(content, filename=file_path)
    
    imports = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.name] = alias.asname if alias.asname else alias.name
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                full_name = f"{node.module}.{alias.name}" if node.module else alias.name
                imports[full_name] = alias.asname if alias.asname else alias.name
    
    used_names = get_used_names(file_path)
    unused_imports = [imp for imp in imports.values() if imp not in used_names]
    
    return unused_imports

def check_invalid_imports(imports):
    invalid_imports = []
    for imp in imports:
        try:
            if '.' in imp:
                components = imp.split('.')
                importlib.import_module(components[0])
            else:
                importlib.import_module(imp)
        except ImportError:
            invalid_imports.append(imp)
    return invalid_imports

def validate_imports(repo_path):
    python_files = find_python_files(repo_path)
    validation_results = {}
    
    for file in python_files:
        unused_imports = find_unused_imports(file)
        if unused_imports:
            validation_results[file] = {
                'unused_imports': unused_imports,
                'invalid_imports': check_invalid_imports(unused_imports)
            }
    
    return validation_results

def display_import_validation_results(validation_results):
    for file, results in validation_results.items():
        print(f'\nFile: {file}')
        if results['unused_imports']:
            print('  Unused Imports:')
            for imp in results['unused_imports']:
                print(f'    {imp}')
        if results['invalid_imports']:
            print('  Invalid Imports:')
            for imp in results['invalid_imports']:
                print(f'    {imp}')

if __name__ == '__main__':
    repo_path = input('Enter the path to the repository: ')
    validation_results = validate_imports(repo_path)
    display_import_validation_results(validation_results)
