from colors_app import *
import time


def Slow(text, delay=0.03):
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


cal = MainColor2(r"""
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


def math_solver():
    Slow(cal)
    print(f"{yellow}Type {red}'exit' {yellow}to leave app!{reset}")
    print(f"{red}Only use this for simple maths!")

    while True:
        expression = input(f"\n{yellow}Enter a math expression {lc}(e.g., 5+3*2): {white}")

        # Exit condition
        if expression.lower() == "exit":
            print(f"{red}Exiting Math Solver...{reset}")
            break

        try:
            result = eval(expression, {"__builtins__": None}, {})  # Restrict eval usage
            print(f"{lc}Result:{white} {result}")
        except Exception as e:
            print(f"{red}Error:{white} {e}")


math_solver()





