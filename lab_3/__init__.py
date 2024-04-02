import re

def is_number(token):
    return re.match(r'^-?\d+(?:\.\d+)?$', token) is not None

def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator == '+':
        values.append(left + right)
    elif operator == '-':
        values.append(left - right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '/':
        values.append(left / right)
    elif operator == '^':
        values.append(left ** right)
    elif operator == '√':
        values.append(left ** (1 / right))

def calculate(expression):
    tokens = re.findall(r'[-+*/^()√]|[A-Za-z]+|\d+\.\d+|\d+', expression)
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '√': 3}
    values = []
    operators = []
    for token in tokens:
        if is_number(token):
            values.append(float(token))
        elif token in precedence:
            while (operators and precedence[operators[-1]] >= precedence[token]):
                apply_operator(operators, values)
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
    while operators:
        apply_operator(operators, values)
    return values[0]

def main():
    while True:
        expression = input("Введите математическое выражение (или 'exit' для выхода): ")
        if expression.lower() == "exit":
            break
        try:
            result = calculate(expression)
            print("Результат:", result)
        except Exception as e:
            print("Ошибка:", e)

if __name__ == "__main__":
    main()
