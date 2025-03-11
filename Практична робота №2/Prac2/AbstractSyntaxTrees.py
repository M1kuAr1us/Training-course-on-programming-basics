import ast
import re
from concurrent.futures import ThreadPoolExecutor

with open('ASTTestFile.py', 'r', encoding='utf-8') as file:
    sourceCode = file.read()
tree = ast.parse(sourceCode)

def FunctionsWithArgs (tree): #Аналіз функцій з аргументами
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            funcName = node.name
            args = [arg.arg for arg in node.args.args]

            functions.append((funcName, args))

    return functions

def ConditionsCount (tree): #Аналіз умов
    conditions = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            conditions += 1

    return conditions

def LoopsCount (tree): #Аналіз циклів
    loops = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.For) or isinstance(node, ast.While):
            loops += 1

    return loops

def AssignmentCount (tree): #Аналіз операторів присвоєння
    assignments = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            assignments += 1

    return assignments

def IsSnake_case (name): #Перевірка змінної на snake_case
    return re.match('^[a-z_][a-z0-9_]*$', name) is not None

def NonStyleVariableSearch (tree): #Аналіз змінних
    variables = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    varName = target.id
                    if not IsSnake_case(varName):
                        variables.add(varName)

        if isinstance(node, ast.NamedExpr):
            varName = node.target.id
            if not IsSnake_case(varName):
                variables.add(varName)

    return variables

def Output():
    print("1) Found functions and their arguments:")
    for funcName, args in getFunctions:
        print(f"Function '{funcName}' ({', '.join(args) if args else 'no arguments'})")

    print("\n2) Conditions, loops and assignments count:")
    print(f" - Conditions (if): {getConditionsCount}")
    print(f" - Loops (for, while): {getLoopsCount}")
    print(f" - Assignments: {getAssignmentsCount}")

    print("\n3) Variables that do not conform to the snake_case style:")
    for varName in getNonStyleVariableSearch:
        print(f" - {varName}")

with ThreadPoolExecutor() as executor: #Багатопоточне виконання функцій.
    getFunctions = FunctionsWithArgs(tree)
    getConditionsCount = ConditionsCount(tree)
    getLoopsCount = LoopsCount(tree)
    getAssignmentsCount = AssignmentCount(tree)
    getNonStyleVariableSearch = NonStyleVariableSearch(tree)

Output()