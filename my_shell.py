import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXTERNAL_COMMANDS = ["ls", "hexdump", "grep", "etc"]


def run_external(command, args):
    bat_path = os.path.join(BASE_DIR, command + ".bat")
    cmd = [bat_path]
    if args:
        cmd.append(args)
    subprocess.call(cmd)

def hello():
    print("hello", os.getlogin())

def cd(path):
    if path == "":
        print(os.getcwd())
        return
    try:
        os.chdir(path)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    while True:
        line = input(os.getcwd() + ">>>").strip()

        if line == "":
            continue

        parts = line.split(maxsplit=1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if command == "exit":
            break
        elif command == "hello":
            hello()
        elif command == "cd":
            cd(args)
        elif command in EXTERNAL_COMMANDS:
            run_external(command, args)
        else:
            print("Unknown command:", command)