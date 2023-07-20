import os
from typing import Optional
import datetime
from pathlib import Path

from dda.yaml.set import load_yaml, update_yaml
from dda.draw.progress import visualize_progress

sd: str = "start_date"
tp: str = "total_pages"
ppd: str = "pages_per_date"
bd: str = "buffer_days"

def set_aim(path_aim_yaml: str)-> None:
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
            aim_dict = _update_aim(aim_dict)
            update_yaml(path_aim_yaml, aim_dict)
    except FileNotFoundError:
        aim_dict = _update_aim()
        update_yaml(path_aim_yaml, aim_dict)

def _communicate_interactive_via_key(dict_set: dict, key: str, value) -> Optional[dict]:
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

def _update_aim(default_dict: Optional[dict] = None) -> dict:
    new_dict: dict = dict()
    if default_dict is not None:
        for key, value in default_dict.items():
            while(True):
                _value = input(f"{key} was {value} : ")
                _ret = _communicate_interactive_via_key(new_dict, key, _value)
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
                _ret = _communicate_interactive_via_key(new_dict, key, _value)
                if type(_ret) == dict:
                    new_dict = _ret
                    print()
                    break
                print()
    return new_dict

def update_progress(path_progress_yaml: str) -> None:
    today = datetime.date.today()
    is_new = False
    if not Path(path_progress_yaml).exists():
        update_yaml(path_progress_yaml, {})
        is_new = True

    progress_data = load_yaml(path_progress_yaml)
    
    if str(today) not in progress_data:
        dates = sorted(list(progress_data.keys()))
        last_date = datetime.datetime.strptime(dates[-1], "%Y-%m-%d").date()
        if not is_new and abs((today-last_date).days) > 1:
            print(f"Enjoy reading and Have Passion!!! (the last date is {dates[-1]})")
            while last_date < today - datetime.timedelta(days=1):
                last_date += datetime.timedelta(days=1)
                progress_data[str(last_date)] = progress_data[dates[-1]]
        pages_read = input("Enter today's reading pages: ")
        progress_data[str(today)] = int(pages_read)
    else:
        current_pages = progress_data[str(today)]
        choice = input(f"Want to Update Today({today})'s value({current_pages})? [y/n]: ")
        if choice.lower() == "y":
            while(True):
                pages_read = input("Enter the new value: ")
                try:
                    progress_data[str(today)] = int(pages_read)
                    break
                except ValueError:
                    print("Please input Positive value")
    
    update_yaml(path_progress_yaml, progress_data)

def draw_from_yaml(aim_path: str, progress_path: str, output_dir: str) -> None:
    aim_dict: dict = load_yaml(aim_path, is_aim=True)
    progress_dict: dict = load_yaml(progress_path)
    today_path: dict = os.path.join(output_dir, str(datetime.date.today())+".png")
    visualize_progress(
        start_date=aim_dict[sd], 
        total_pages=aim_dict[tp], 
        pages_per_day_goal=aim_dict[ppd], 
        input_data=progress_dict, buffer_days=aim_dict[bd], save_path=today_path
    )

if __name__ == "__main__":
    aim_path:str = "../tmp_files/main.set_main.yaml"    
    # from subprocess import run
    # run(f"rm {edit_path}", shell=True)
    # set_aim(edit_path)
    progress_path:str = "../tmp_files/main.progress.yaml"   
    # update_progress(edit_path)
    output_dir:str = "../tmp_files"
    draw_from_yaml(aim_path, progress_path, output_dir)
