import os
import libcst as cst

flask_repo_path = "./flask-main"  # 用实际的 Flask 仓库路径替换

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

def explore_module_structure(module):
    classes, functions, imports = extract_classes_functions_imports(module)

    print(f"Classes in module: {len(classes)}")
    for class_node in classes:
        print(f"  - {class_node.name}")

    print(f"\nFunctions in module: {len(functions)}")
    for function_node in functions:
        print(f"  - {function_node.name}")

    print(f"\nImports in module: {len(imports)}")
    for import_node in imports:
        print(f"  - {import_node}")

def main():
    for root, dirs, files in os.walk(flask_repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                module = analyze_code(file_path)
                print(f"\nAnalyzing module: {file_path}")
                explore_module_structure(module)

if __name__ == "__main__":
    main()