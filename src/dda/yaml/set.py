import yaml

def update_yaml(file_path: str, data: dict) -> None:
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def load_yaml(file_path: str) -> dict:
    data: dict
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def complete_yaml(file_path: str, default_data: dict) -> dict:
    data: dict
    try:
        data = load_yaml(file_path)
        for key, value in default_data.items():
            if key not in data:
                data[key] = value
    except FileNotFoundError:
        data = default_data
    update_yaml(file_path, data)
    return data

