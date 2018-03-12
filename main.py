import dsstore
import os
import sys

if __name__ == "__main__":
    if not os.path.exists(sys.argv[1]):
        sys.exit("File not found: Usage main.py <file>")
    with open(sys.argv[1], "rb") as f:
        d = dsstore.DS_Store(f.read(), debug=False)
        files = d.traverse_root()
        print("Count: ", len(files))
        for f in files:
            print(f)

