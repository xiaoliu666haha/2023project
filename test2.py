import os
import libcst as cst

flask_repo_path = "./flask-main"  # 用实际的 Flask 仓库路径替换
output_file_path = "./output_1.txt"  # 指定输出文件路径

def analyze_code(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    module = cst.parse_module(code)
    return module

def extract_classes_functions_imports(node):
    classes = [c for c in node.body if isinstance(c, cst.ClassDef)]
    functions = [f for f in node.body if isinstance(f, cst.FunctionDef)]
    imports = [i for i in node.body if isinstance(i, cst.Import) or isinstance(i, cst.ImportFrom)]

    return classes, functions, imports

def explore_module_structure(module, output_file):
    classes, functions, imports = extract_classes_functions_imports(module)

    output_file.write(f"Classes in module: {len(classes)}\n")
    for class_node in classes:
        output_file.write(f"  - {class_node.name}\n")

    output_file.write(f"\nFunctions in module: {len(functions)}\n")
    for function_node in functions:
        output_file.write(f"  - {function_node.name}\n")

    output_file.write(f"\nImports in module: {len(imports)}\n")
    for import_node in imports:
        output_file.write(f"  - {import_node}\n")

def main():
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for root, dirs, files in os.walk(flask_repo_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    module = analyze_code(file_path)
                    output_file.write(f"\nAnalyzing module: {file_path}\n")
                    explore_module_structure(module, output_file)

if __name__ == "__main__":
    main()

