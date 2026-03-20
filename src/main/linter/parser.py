import yaml

def load_yaml(file_path):
    try:
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)
            if not data:
                raise Exception("Empty YAML file")
            return data
    except Exception as e:
        raise Exception(f"YAML Error: {str(e)}")