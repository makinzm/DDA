import argparse
import os

from sub_main import set_aim, update_progress, draw_from_yaml

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["aim", "progress"], help="Command to execute")
    parser.add_argument("-r", "--root", action="store_true", help="Use current CLI root path")
    args = parser.parse_args()

    path = os.path.join(os.path.dirname(os.path.dirname(os.path.join(__file__))),"resources")
    if args.root:
        path = os.getcwd()
    aim_path = os.path.join(path,"aim.yaml")
    progress_path = os.path.join(path, "progress.yaml")
    print(aim_path, progress_path)
    
    if args.command == "aim":
        set_main()
    elif args.command == "progress":
        update_progress(progress_path)
        draw_from_yaml(aim_path, progress_path, path)
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
