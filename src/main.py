from typing import Optional
import datetime

from dda.yaml.set import load_yaml, update_yaml

sd: str = "start_date"
tp: str = "total_pages"
ppd: str = "pages_per_date"
bd: str = "buffer_days"

def set_main(path_aim_yaml: str)-> None:
    aim_dict: dict
    try:
        aim_dict = load_yaml(path_aim_yaml, is_aim=True)
        yn: str
        while(True):
            yn = input(f"Do you want to update {path_aim_yaml}?(y/n) : ")
            if yn in set(["y","n"]):
                break
            else:
                print("Please input (y/n) \n")
        if yn == "y":
            aim_dict = update_aim(aim_dict)
            update_yaml(path_aim_yaml, aim_dict)
    except FileNotFoundError:
        aim_dict = update_aim()
        update_yaml(path_aim_yaml, aim_dict)

def communicate_interactive_via_key(dict_set: dict, key: str, value) -> Optional[dict]:
    if key == sd:
        try:
            value = datetime.date.fromisoformat(value)
            dict_set[key] = value
            return dict_set
        except ValueError:
            print("Please Input Date like `2023-07-16`")
            return None
    else:
        try:
            value = int(value)
            if value > 0:
                dict_set[key] = value
                return dict_set
            else:
                raise ValueError
        except ValueError:
            print("Please positive value like `10`")
            return None

def update_aim(default_dict: Optional[dict] = None) -> dict:
    new_dict: dict = dict()
    if default_dict is not None:
        for key, value in default_dict.items():
            while(True):
                _value = input(f"{key} was {value} : ")
                _ret = communicate_interactive_via_key(new_dict, key, _value)
                if type(_ret) == dict:
                    new_dict = _ret
                    print()
                    break
                print()
    else:
        keys: list[str] = [sd, tp, ppd, bd]
        for key in keys:
            while(True):
                _value = input(f"{key} : ")
                _ret = communicate_interactive_via_key(new_dict, key, _value)
                if type(_ret) == dict:
                    new_dict = _ret
                    print()
                    break
                print()
    return new_dict

if __name__ == "__main__":
    edit_path:str = "../tmp_files/main.set_main.yaml"    
    from subprocess import run
    # run(f"rm {edit_path}", shell=True)
    set_main(edit_path)
