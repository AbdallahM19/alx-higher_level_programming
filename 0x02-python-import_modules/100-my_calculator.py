#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = (sys.argv[3])
    if operator == '+':
        result = add(int(a), int(b))
    elif operator == '-':
        result = sub(int(a), int(b))
    elif operator == '*':
        result = mul(int(a), int(b))
    elif operator == '/':
        result = div(int(a), int(b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))


