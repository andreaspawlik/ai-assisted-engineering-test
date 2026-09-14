import argparse
import sys


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float)
    add_parser.add_argument("b", type=float)

    subtract_parser = subparsers.add_parser("subtract", help="Subtract two numbers")
    subtract_parser.add_argument("a", type=float)
    subtract_parser.add_argument("b", type=float)

    multiply_parser = subparsers.add_parser("multiply", help="Multiply two numbers")
    multiply_parser.add_argument("a", type=float)
    multiply_parser.add_argument("b", type=float)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        print(add(args.a, args.b))
        return 0

    if args.command == "subtract":
        print(subtract(args.a, args.b))
        return 0

    if args.command == "multiply":
        print(multiply(args.a, args.b))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
