import argparse
import os

from dda.sub_main import set_aim, update_progress, draw_from_yaml
from dda.yaml.set import load_yaml, update_yaml

def main():
    saved_config_path = os.path.join(os.path.dirname(os.path.join(__file__)),"config.yaml")
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["aim", "progress", "get-config", "set-config"], help="Command to execute")
    parser.add_argument("-r", "--root", action="store_true", help="Use current CLI root path")
    args = parser.parse_args()
    if args.root:
        path = os.getcwd()
    else:
        config_data = load_yaml(saved_config_path)
        path = config_data["path"]
    aim_path = os.path.join(path,"aim.yaml")
    progress_path = os.path.join(path, "progress.yaml")
    print(aim_path, progress_path)
    
    if args.command == "aim":
        set_aim(aim_path)
    elif args.command == "progress":
        update_progress(progress_path)
        draw_from_yaml(aim_path, progress_path, path)
    elif args.command == "get-config":
        config_data = load_yaml(saved_config_path)
        print(config_data)
    elif args.command == "set-config":
        config_data = load_yaml(saved_config_path)
        print("Current : ", config_data)
        new_path = input("Please Input New Resource Path : ")
        new_config = {"path": new_path}
        update_yaml(saved_config_path, new_config)
        config_data = load_yaml(saved_config_path)
        print("Completed : ", config_data)
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
