import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("The syntax of the command is incorrect.")
    else:
        try:
            with open(sys.argv[1], "rb") as f:
                data = f.read()
            for offset in range(0, len(data), 16):
                chunk = data[offset:offset + 16]
                hex_part = " ".join(f"{b:02x}" for b in chunk)
                text = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
                print(f"{offset:04x}  {hex_part:<47}  {text}")
        except FileNotFoundError:
            print("The system cannot find the file specified.")
        except PermissionError:
            print("Access is denied.")