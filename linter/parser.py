import yaml

def load_yaml(file_path):
    try:
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise Exception(f"YAML Error: {str(e)}")
    