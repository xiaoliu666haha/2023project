from pathlib import Path
from libcst import parse_module, CSTNode, CSTVisitor, Call

# 定义一个访问器来查找特定模式
class CustomAnalyzer(CSTVisitor):
    def __init__(self):
        super().__init__()  # 调用父类的构造函数
        self.function_calls = []

    def visit_Call(self, node: "Call") -> None:
        # 检查是否是函数调用
        if isinstance(node.func, CSTNode):
            self.function_calls.append(node.func)
        super().visit_Call(node)  # 调用父类的方法

def analyze_flask_codebase(flask_repo_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        # 遍历 Flask 代码库中的所有 Python 文件
        for python_file in flask_repo_path.glob("**/*.py"):
            with python_file.open("r", encoding="utf-8") as file:
                try:
                    # 尝试解析当前文件
                    module = parse_module(file.read())

                    # 初始化自定义分析器
                    analyzer = CustomAnalyzer()
                    module.visit(analyzer)

                    # 输出分析结果到文件
                    output.write(f"File analyzed: {python_file}\n")
                    output.write(f"Function calls found: {analyzer.function_calls}\n")
                    output.write("\n")

                except Exception as e:
                    output.write(f"Error analyzing {python_file}: {e}\n")

def main():
    # Flask 代码库的根目录
    flask_repo_path = Path("./flask-main")
    output_file = "call_result.txt"
    analyze_flask_codebase(flask_repo_path, output_file)

if __name__ == "__main__":
    main()