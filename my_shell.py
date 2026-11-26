import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXTERNAL_COMMANDS = ["ls", "hexdump", "grep", "etc"]


def run_external(command, args, input_data=None, capture=False):
    bat_path = os.path.join(BASE_DIR, command + ".bat")
    cmd = [bat_path]
    if args:
        cmd.extend(args.split())
    result = subprocess.run(cmd, input=input_data, text=True, capture_output=capture)
    return result.stdout

def run_pipe(line):
    out_file = None
    if ">" in line:
        line, out_file = line.split(">", 1)
        out_file = out_file.strip()

    segments = [s.strip() for s in line.split("|")]
    data = None
    for i, segment in enumerate(segments):
        parts = segment.split(maxsplit=1)
        if not parts or parts[0].lower() not in EXTERNAL_COMMANDS:
            print("Unknown command:", segment)
            return
        args = parts[1] if len(parts) > 1 else ""
        data = run_external(parts[0].lower(), args, data, capture=(i < len(segments) - 1 or out_file is not None))

    if out_file:
        with open(out_file, "w") as f:
            f.write(data)


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
        if "|" in line or ">" in line:
            run_pipe(line)
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