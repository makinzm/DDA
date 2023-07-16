import datetime
import yaml

sd: str = "start_date"

def update_yaml(file_path: str, data: dict) -> None:
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def load_yaml(file_path: str, is_aim: bool = False) -> dict:
    data: dict
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        if is_aim:
            data[sd] = datetime.date.fromisoformat(str(data[sd]))
    return data

def complete_yaml(file_path: str, default_data: dict) -> dict:
    data: dict
    try:
        data = load_yaml(file_path, is_aim=False)
        if type(data) == dict:
            if set(data.keys()) == set(default_data.keys()):
                for key, value in default_data.items():
                    if key not in data.keys():
                        data[key] = value
            else:
                data = default_data
        else:
            data = default_data
    except FileNotFoundError:
        data = default_data
    update_yaml(file_path, data)
    return data

