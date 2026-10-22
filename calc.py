import json
import sys


def calc(a: int, op: str, b: int) -> int | str | float:
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case "%":
            return a % b
        case "//":
            return a // b
        case _:
            return "Ожидался правильный знак"


def load_history() -> list:
    try:
        with open("history.json") as f:
            json_history = json.load(f)
    except FileNotFoundError:
        json_history = []
    return json_history


expression = sys.argv[1]
if expression == "--history":
    new_result = load_history()
    new_result_ten = new_result[-10:]
    for i in new_result_ten:
        print(i)
elif expression == "--clear":
    with open("history.json", "w") as f:
        clear_history = []
        json.dump(clear_history, f)
else:
    expression1 = expression.split()
    new_list = []
    flag = False
    for i in range(len(expression1)):
        if (
            expression1[i] == "*"
            or expression1[i] == "/"
            or expression1[i] == "%"
            or expression1[i] == "//"
        ):
            flag = True
            left_number = new_list.pop()
            right_number = expression1[i + 1]
            result_number = calc(int(left_number), expression1[i], int(right_number))
            new_list.append(result_number)
        elif flag:
            flag = False
            continue
        else:
            new_list.append(expression1[i])
    first_number = new_list[0]
    for i in range(1, len(new_list), 2):
        first_number = calc(int(first_number), new_list[i], int(new_list[i + 1]))

    line = f"Исходное выражение: {expression} = Итог: {first_number}"
    print(line)
    json_history = load_history()

    json_history.append(line)
    with open("history.json", "w") as f:
        json_history = json_history[-50:]
        json.dump(json_history, f)
