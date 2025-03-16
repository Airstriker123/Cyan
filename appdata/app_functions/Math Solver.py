from colors_app import *
import time
import sympy as sp
import re
import math


def Slow(text, delay=0.02):
    for line in text.split("\n"):
        print(line, flush=True)
        time.sleep(delay)


def MainColor2(text):
    start_color = (0, 200, 150)
    end_color = (0, 255, 255)

    num_steps = 16
    colors = [
        (
            start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1),
            start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1),
            start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1),
        )
        for i in range(num_steps)
    ]
    colors += list(reversed(colors[:-1]))

    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    result = []
    lines = text.split("\n")
    for i, line in enumerate(lines):
        color_index = i % len(colors)
        r, g, b = colors[color_index]
        colored_line = text_color(r, g, b) + line + "\033[0m"
        result.append(colored_line)

    return "\n".join(result)


def safe_eval(expression):
    expression = expression.replace('^', '**')
    expression = re.sub(r'(\d+)!', r'math.factorial(\1)', expression)

    allowed_funcs = {
        "sin": sp.sin,
        "cos": sp.cos,
        "tan": sp.tan,
        "sqrt": sp.sqrt,
        "log": sp.log,
        "ln": lambda x: sp.log(x, sp.E),
        "exp": sp.exp,
        "pi": sp.pi,
        "e": sp.E,
        "factorial": math.factorial,
        "abs": abs,
        "round": round
    }
    try:
        result = sp.sympify(expression, locals=allowed_funcs).evalf()
        return round(result, 10) if isinstance(result, (int, float)) else result
    except Exception:
        return "Invalid Expression"


def math_solver():
    cal = MainColor2("""
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████                           █████
 █████                           █████
 █████                           █████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 █████████████████████████████████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 ████████    ████    ████    █████████
 █████████████████████████████████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 █████████████████████████████████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████

""")
    Slow(cal)
    print(f"{yellow}Type {red}'exit' {yellow}to leave app!{reset}")
    print(f"{purple}Supports:{cyan} +, -, *, /, ^, !, sin(), cos(), tan(), sqrt(), log(), ln(), exp(), pi, e, abs(), round()")

    while True:
        expression = input(f"\n{yellow}Enter a math expression {lc}(e.g., 5+3*2, 4!): {white}")
        if expression.lower() == "exit":
            print(f"{red}Exiting Math Solver...{reset}")
            break

        result = safe_eval(expression)
        print(f"{lc}Result:{white} {result}")

math_solver()
