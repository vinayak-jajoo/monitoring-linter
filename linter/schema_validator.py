import json
from jsonschema import validate, ValidationError

def validate_schema(data, schema_path):
    try:
        with open(schema_path, "r") as f:
            schema = json.load(f)

        validate(instance=data, schema=schema)
        return []

    except ValidationError as e:
        return [f"Schema Validation Error: {e.message}"]

    except Exception as e:
        return [f"Schema Error: {str(e)}"]