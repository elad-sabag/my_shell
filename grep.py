import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("The syntax of the command is incorrect.")
    else:
        search = sys.argv[1]
        try:
            if len(sys.argv) > 2:
                with open(sys.argv[2], "r", errors="replace") as f:
                    lines = f.readlines()
            else:
                lines = sys.stdin.readlines()
            for number, line in enumerate(lines, 1):
                if search in line:
                    print(f"{number}: {line.rstrip()}")
        except FileNotFoundError:
            print("The system cannot find the file specified.")
        except PermissionError:
            print("Access is denied.")