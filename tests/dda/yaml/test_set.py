from pathlib import Path

from dda.yaml.set import complete_yaml

def test_complete_yaml():
    file_path = "data.yaml"
    default_data = {
        "start_date": "2023-07-16",
        "total_pages": 500,
        "pages_per_day": 10,
        "buffer_days": 0
    }

    test_dir = Path("tmp_files")
    test_dir.mkdir(exist_ok=True)
    yaml_file = test_dir / file_path
    yaml_file.touch()

    data = complete_yaml(yaml_file, default_data)

    print("")
    for k,v in default_data.items():
        print(k,type(v),v)
    print("-----")
    for k,v in data.items():
        print(k,type(v),v)

    assert data == default_data

    yaml_file.unlink()
