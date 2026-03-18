import sys
from linter.parser import load_yaml
from linter.schema_validator import validate_schema
from linter.rules import RuleEngine
from linter.reporter import generate_report

SCHEMA_PATH = "schemas/prometheus_schema.json"

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m linter.main <file.yaml>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        data = load_yaml(file_path)
    except Exception as e:
        print(e)
        sys.exit(1)

    # Schema validation
    schema_errors = validate_schema(data, SCHEMA_PATH)

    # Rule checks
    engine = RuleEngine()
    errors, warnings, info = engine.run(data)

    errors.extend(schema_errors)

    generate_report(errors, warnings, info)


if __name__ == "__main__":
    main()