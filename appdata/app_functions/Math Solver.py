from colors_app import *


def math_solver():
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





