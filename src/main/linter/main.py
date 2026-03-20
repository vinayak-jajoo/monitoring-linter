import sys
import os

from src.main.linter.rules import RuleEngine
from src.main.linter.reporter import generate_report


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m src.main.linter.main <config.cfg>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: File not found -> {file_path}")
        sys.exit(1)

    try:
        with open(file_path, "r") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    engine = RuleEngine()
    errors, warnings, info = engine.run_nagios_config(content)

    generate_report(errors, warnings, info)

    if errors:
        print("\n[CI/CD] Lint failed.")
        sys.exit(1)
    else:
        print("\n[CI/CD] Lint passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()