import os
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "."

    try:
        for name in os.listdir(path):
            print(name)
    except FileNotFoundError:
        print("The system cannot find the path specified.")
    except NotADirectoryError:
        print("The directory name is invalid.")
    except PermissionError:
        print("Access is denied.")